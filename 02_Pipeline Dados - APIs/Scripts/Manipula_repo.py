import requests
import base64
import os
from dotenv import load_dotenv


class ManipulaRepositorios:

        def __init__(self):
            load_dotenv(dotenv_path='/home/fe/Documentos/Git/Engenharia-de-Dados/02_Pipeline Dados - APIs/config/.env')
            access_token = os.getenv('GITHUB_ACCESS_TOKEN')
            usuario_name = os.getenv('GITHUB_USUARIO')

            self.username = usuario_name
            self.api_base_url = 'https://api.github.com'
            self.access_token = access_token
            self.headers = {'Authorization':"Bearer " + self.access_token}


        def cria_repo(self, nome_repo):
            data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": True
            }
            response = requests.post(f"{self.api_base_url}/user/repos",
            json=data, headers=self.headers)

            print(f'status_code criação do repositório: {response.status_code}')

        def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):

            # Codificando o arquivo
            with open(caminho_arquivo, "rb") as file:
                file_content = file.read()
            encoded_content = base64.b64encode(file_content)

            # Realizando o upload
            url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
            data = {
            "message": "Adicionando um novo arquivo",
            "content": encoded_content.decode("utf-8")
            }

            response = requests.put(url, json=data, headers=self.headers)
            print(f'status_code upload do arquivo: {response.status_code}')

# instanciando um objeto
novo_repo = ManipulaRepositorios()

# Criando o repositório
nome_repo = 'Armazenamento_Projeto02'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', '/home/fe/Documentos/Git/Engenharia-de-Dados/02_Pipeline Dados - APIs/dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', '/home/fe/Documentos/Git/Engenharia-de-Dados/02_Pipeline Dados - APIs/dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', '/home/fe/Documentos/Git/Engenharia-de-Dados/02_Pipeline Dados - APIs/dados/linguagens_spotify.csv')