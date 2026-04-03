# Engenharia-de-Dados
Passo a passo
Contextualização: Duas empresas se unem e precisam ver seus dados juntos, porém uma das empresas envia em Json e outro em CSV. É preciso unir as duas informações

1. Criação da estrutura das pastas
    - Data Raw - Camada Bronze - Dados Brutos
    - Notebooks - Camada Silver - Processamento dos dados
    - Data Processed  - Camada Gold - Dados prontos para analises

2. Criação do ambiente python de desenvolvimento
    Comandos ultilizados:
        - sudo apt-get update
        - sudo apt-get upgrade -y
        - sudo apt install python3-pip -y
        - python3 -m venv .venv
        - source .venv/bin/activate
        - pip install notebook==7.0.3 ipykernel

3. Processo ETL
        - Leitura dos dados
        - Identificação problemas
        - Tratatamento
        - Criação de um novo csv com as bases unidas

