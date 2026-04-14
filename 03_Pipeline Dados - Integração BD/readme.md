
# Pipeline de Engenharia de dados 
Fluxo do projeto: API -> MOngo DB -> Transformação -> MySql

## 1 - CONFIGURANDO D0 AMBIENTE PYTHON

### Comandos Ultilizados
- sudo apt update
- sudo apt upgrade -y
- sudo apt install python3-pip -y
- sudo apt install python3-venv -y
- python3 -m venv venv
- source venv/bin/activate
- pip install requests==2.31.0
- pip install pymongo==4.4.0
- pip install pandas
- pip install mysql-connector-python==8.0.33
- pip install python-dotenv



## 2 - CONFIGURANDO MONGODB
- Criação do cluster via mongo DB Atlas
- Criação do usuario
Comandos: 
    - python -m pip install "pymongo[srv]"

## 3 - PROCESSO ETL INICIAL
- Extração do dados da API
- Conectando no mongoDB
- Inserindo os dados da API no BD