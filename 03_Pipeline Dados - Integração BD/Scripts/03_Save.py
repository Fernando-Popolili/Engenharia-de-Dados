from dotenv import load_dotenv
import os
import pandas as pd
import mysql.connector
from time import sleep

# 1 - connect_mysql(host_name, user_name, pw): estabelece a conexão com o servidor MySQL, utilizando os dados do host, usuário e senha. A função deve retornar a conexão estabelecida.

#2 - create_cursor(cnx): cria e retorna um cursor, que serve para conseguirmos executar os comandos SQL, utilizando a conexão fornecida como argumento.

#3 - create_database(cursor, db_name): cria um banco de dados com o nome fornecido como argumento. Para isso, a função deverá usar o cursor para executar o comando SQL de criação do banco de dados.

#4 - show_databases(cursor): exibe todos os bancos de dados existentes. Para isso, a função deve utilizar o cursor para executar o comando SQL que lista todos os bancos de dados existentes.

#5 - create_product_table(cursor, db_name, tb_name): cria uma tabela com o nome fornecido no banco de dados especificado. A tabela deve ter as colunas que correspondam aos dados que serão inseridos posteriormente.

#6 - show_tables(cursor, db_name): lista todas as tabelas existentes no banco de dados especificado. Para isso, a função deve utilizar o cursor para executar o comando SQL que lista todas as tabelas no banco de dados.

#7 - read_csv(path): lê um arquivo csv do caminho fornecido e retorna um DataFrame do pandas com esses dados.

#8 - add_product_data(cnx, cursor, df, db_name, tb_name): insere os dados do DataFrame fornecido à tabela especificada no banco de dados especificado. A função deve usar o cursor para executar o comando SQL de inserção de dados.



class Main:
    def __init__(self):
            load_dotenv('/home/fe/Documentos/Git/Engenharia-de-Dados/03_Pipeline Dados - Integração BD/config/.env')  # caminho do seu arquivo
            self.user_mysql = os.getenv("user_mysql")
            self.password_mysql = os.getenv("password_mysql")


    def connect_mysql(self):

        cnx = mysql.connector.connect(
            host = 'localhost',
            user = self.user_mysql,
            password = self.password_mysql
        )
        return cnx
    
    def create_cursor(self, cnx):
        cursor = cnx.cursor()
        return cursor
    
    def create_db(self, cursor, DB_NAME):
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
    
    def show_db(self, cursor):
        cursor.execute("SHOW DATABASES;")
        lista_db = []
        for db in cursor:
            lista_db.append(db)
        return lista_db

    def create_product_table(self, cursor, db_name, tb_name):
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {db_name}.{tb_name}(
                    id VARCHAR(100),
                    Produto VARCHAR(100),
                    Categoria_Produto VARCHAR(100),
                    Preco FLOAT(10,2),
                    Frete FLOAT(10,2),
                    Data_Compra DATE,
                    Vendedor VARCHAR(100),
                    Local_Compra VARCHAR(100),
                    Avaliacao_Compra INT,
                    Tipo_Pagamento VARCHAR(100),
                    Qntd_Parcelas INT,
                    Latitude FLOAT(10,2),
                    Longitude FLOAT(10,2),
                    
                    PRIMARY KEY (id));
        """)

    def show_tables(self, cursor, db_name):
        cursor.execute(f"USE {db_name};")
        cursor.execute("SHOW TABLES;")

        for tb in cursor:
            print(tb)

    def read_csv(self, path): 
        df = pd.read_csv(path)
        return df

    def add_product_data(self, cnx, cursor, df, db_name, tb_name):
        lista_dados = [tuple(row) for i, row in df.iterrows()]
        sql = f"INSERT INTO {db_name}.{tb_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.executemany(sql, lista_dados)
        cnx.commit()
       

#Inicio
print('Conectando ao Mysql....')
sleep(1.5)

App = Main()

#Conectar MySQl
cnx = App.connect_mysql()
print(cnx)
cursor = App.create_cursor(cnx)

#Criar DB
db_name = input("Qual nome do Banco de dados: ")
App.create_db(cursor, db_name)
print("\n\nTodos os BD existentes: ")
lista_db = App.show_db(cursor)
for db in lista_db:
    print(db)

#Criar Tabela
tb_name = input("\n\nQual o nome da Tabela: ")
App.create_product_table(cursor, db_name, tb_name)
print("\n\nTodos as Tabelas existentes: ")
App.show_tables(cursor, db_name)

#Criar Dados para Inserção
path = "/home/fe/Documentos/Git/Engenharia-de-Dados/03_Pipeline Dados - Integração BD/Data/TB_PRODUTOS_2021.csv"
df = App.read_csv(path)

#Inserir Dados
App.add_product_data(cnx, cursor, df, db_name, tb_name)

print(cursor.rowcount, "dados foram inseridos.")