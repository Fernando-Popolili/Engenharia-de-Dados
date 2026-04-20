
# Pipeline de Engenharia de dados 
Fluxo do projeto: API -> MOngo DB -> Transformação -> MySql


## 00 - Configuração Pastas

03_PIPELINE DADOS - INTEGRAÇÃO BD/
│
├── config/
│   └── .env                  # Variáveis de ambiente (credenciais, conexões)
│
├── Data/
│   ├── TB_ESPORTE_LAZER.csv
│   ├── TB_LIVROS.csv
│   └── TB_PRODUTOS_2021.csv  # Arquivos de dados tratados no pipeline
│
├── Notebooks/
│   ├── 01_ETL_Inicial.ipynb    # Extração e carga inicial (API → MongoDB)
│   ├── 02_Transformacao.ipynb  # Tratamento e transformação dos dados
|   └── 03_Salvar_mySQL.ipynb   # Inserção no MySQL
│
├── Scripts/
│   ├── 01_Extracao.py       # Script de extração (API → MongoDB)
│   ├── 02_Transformacao.py  # Script de transformação dos dados
│   └── 03_Save.py           # Script de carga (MySQL)
│
├── venv/                    # Ambiente virtual Python
│
└── readme.md               # Documentação do projeto
    

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
- sudo apt install mysql-server-8.0 -y
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

## 4 - Tranformação
- EXtrair os dados do Mongo DB
- Renomear colunas
- Arrumar datas

## 5 - Inserir dados tratados no Mysql
- Conexão com o MySQL
- Criação de usuario ADMIN
- Criar Banco de Dados
- Criar Tabela
- Inserir Dados transformados

## 6 - Criação de Scripts
- Criação de Scripts .PY sobre os Notebooks .IPYNB com o objetivo de resumir e deixar o codigo mais legivéis para futuros processos ETLs