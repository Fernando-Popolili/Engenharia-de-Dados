# Engenharia-de-Dados

### Contextualização
Duas empresas se unem e precisam ver seus dados juntos, porém:
- Uma envia dados em JSON  
- Outra envia dados em CSV  

É necessário unir as duas informações.

---

### 1. Criação da estrutura das pastas
- Data Raw → Camada Bronze → Dados brutos  
- Notebooks → Camada Silver → Processamento dos dados  
- Data Processed → Camada Gold → Dados prontos para análise  

---

### 2. Criação do ambiente Python de desenvolvimento

Comandos utilizados:
- sudo apt-get update  
- sudo apt-get upgrade -y  
- sudo apt install python3-pip -y  
- python3 -m venv .venv  
- source .venv/bin/activate  
- pip install notebook==7.0.3 ipykernel  

---

### 3. Processo ETL
- Leitura dos dados  
- Identificação de problemas  
- Tratamento dos dados  
- Criação de um novo CSV com as bases unidas  

### 34. Processo ETL simplificado - Tornando o processo mais reutilizavel com classes e funções
- Leitura dos dados  
- Identificação de problemas  
- Tratamento dos dados  
- Criação de um novo CSV com as bases unidas  
