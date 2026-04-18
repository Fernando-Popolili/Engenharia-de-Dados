from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

#Funções:
class Main:
    #Inicio
    def __init__(self, nomeDB, nome_collection):
        load_dotenv('/home/fe/Documentos/Git/Engenharia-de-Dados/03_Pipeline Dados - Integração BD/config/.env')  # caminho do seu arquivo
        user = os.getenv("user")
        password = os.getenv("password")
        api_url = 'https://jsonplaceholder.typicode.com/posts'

        self.nomeDB = nomeDB
        self.nome_collection = nome_collection
        self.api_url = api_url
        self.user = user
        self.password = password
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