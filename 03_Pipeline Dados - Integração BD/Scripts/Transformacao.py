from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

#Funções:
class Main:
    #Inicio
    def __init__(self, nomeDB, nome_collection):
        # .ENV
        load_dotenv('/home/fe/Documentos/Git/Engenharia-de-Dados/03_Pipeline Dados - Integração BD/config/.env')  
        user = os.getenv("user")
        password = os.getenv("password")
        self.user = user
        self.password = password

        #URL DA API
        api_url = 'https://jsonplaceholder.typicode.com/posts'
        self.api_url = api_url

        #BANCO DE DADOS
        self.nomeDB = nomeDB
        self.nome_collection = nome_collection

        
        #URL DO MONGODB
        self.uri = f"mongodb+srv://{user}:{password}@cluster-pipeline.ehjptg7.mongodb.net/?appName=Cluster-pipeline"

    #Conexão
    def connect_mongo(self):
        # Create a new client and connect to the server
        client = MongoClient(self.uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            print(self.uri)
            print(self.user)
        except Exception as e:
            print(e)
        
        self.client = client

    #Conexão no banco
    def conectando_db(self):
        db = self.client[self.nomeDB]
        collection = db[self.nome_collection]
        self.collection = collection


    #Listar dados do banco
    def listar_dados(self):
        for doc in self.collection.find_one():
            print(doc)

    #Listar Colunas
    def listar_colunas(self):
        lista_colunas = []
        for documento in self.collection.find_one():
            lista_colunas.append(documento)
        return lista_colunas

    #Renomear colunas
    def renomear_coluna(self, nome_coluna, novo_nome_coluna):
        self.collection.update_many({}, {"$rename":{nome_coluna: novo_nome_coluna}})

    #Listar categoria
    def listar_categorias(self):
        lista_categorias = self.collection.distinct("Categoria do Produto")
        return lista_categorias
    #Selecionar categoria especifica

    def filtrar_categoria(self, item):
        query = {"Categoria do Produto": f"{item}"}
        livros = self.collection.find(query)
        lista_livros = []
        for doc in livros:
            lista_livros.append(doc)
        return lista_livros

    #Criar dataframe
    def criar_df(self, lista):
        df = pd.DataFrame(lista)
        return df
    
    def salva_arquivo_csv(self, df, nome_tabela):
        df.to_csv(f"/home/fe/Documentos/Git/Engenharia-de-Dados/03_Pipeline Dados - Integração BD/Data/{nome_tabela}.csv", index=False)


    

nomeDB = input("Qual o nome do banco: ")
nome_collection = input("Qual o nome da collection: ")

app = Main(nomeDB, nome_collection)
app.connect_mongo()
app.conectando_db()
app.listar_dados()

#Renomear coluna
lista_colunas = app.listar_colunas()
print("\n \n Nome das colunas: ")
for i in lista_colunas:
    print(i)
resp = input("Deseja renomear alguma coluna? (S/N) ")
if resp == "S":  
    nome_coluna = input("Digite o nome da coluna: ")
    novo_nome_coluna = input("Digite o novo nome da coluna: ")
    #Se a coluna existir
    if nome_coluna in lista_colunas:
        app.renomear_coluna(nome_coluna, novo_nome_coluna)
        print("Coluna renomeada com sucesso!")
    #Se não existir
    else:
        print("Coluna não encontrada")

#Criar Query e salvar csv
filtrar = input("\n \nDeseja filtrar alguma categoria de produto? (S/N)  ")
if filtrar == "S":
    categorias = app.listar_categorias()
    print(categorias)

    filtro = input("Qual categoria deseja filtrar? ")
    tb_livros = app.filtrar_categoria(filtro)

    df_criado = app.criar_df(tb_livros)

    nome_tabela = input("Qual nome deseja salvar a tabela: ")
    app.salva_arquivo_csv(df_criado, nome_tabela)

