
# 🚫 Code Against Fraud  
**Machine Learning + Engenharia de Dados Aplicada à Detecção de Fraudes**

🔗 Projeto integrante do **Small Data Lab**. Este projeto tem como objetivo construir um pipeline robusto de detecção de fraudes utilizando boas práticas de engenharia de dados, modelagem supervisionada e preparação eficiente dos dados.

---

## 🎯 Objetivo  
- Estruturar um pipeline completo para detecção de fraudes.  
- Aplicar boas práticas de MLOps desde a preparação dos dados.  
- Realizar análise exploratória (EDA) com foco na compreensão do comportamento das fraudes.  
- Desenvolver pipelines modulares e reprodutíveis.  
- Realizar modelagem supervisionada com foco na detecção de fraudes.  

---

## 🚀 Pipeline  

| Etapa                 | Descrição                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------|
| **Data Preparation**   | Conversão do CSV para DuckDB, ingestão dos dados e preparação inicial.                        |
| **EDA (Análise)**      | Análise exploratória dos dados, verificação de padrões, distribuições e balanceamento.        |
| **Feature Engineering**| Desenvolvimento de novas variáveis baseadas em comportamento, estatísticas e dados temporais. |
| **Modelagem**          | Treinamento de modelos supervisionados (Logistic, RandomForest, XGBoost).                     |
| **Avaliação**          | Avaliação de performance dos modelos com métricas clássicas e de negócio.                     |

---

## 📂 Estrutura de Pastas  

```plaintext
codeagainstfraud/
├── data/                   
│   ├── raw/                # Dados brutos (não sobe)
│   ├── interim/            # Banco DuckDB (sobe)
│   └── processed/          # Dados processados finais (não sobem)
├── notebooks/              
├── pipelines/              
├── reports/                
├── requirements.txt        
├── README.md               
└── .gitignore              
```

---

## 🔍 Dataset  
- **Fonte:** [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
- **Descrição:** Dataset com 284.807 transações, sendo 492 fraudes (dados altamente desbalanceados).  

> ⚠️ **Observação:**  
> O arquivo CSV original não está presente no repositório devido às limitações de tamanho do GitHub.  
> O banco DuckDB (`fraud_data.duckdb`) está disponível na pasta `/data/interim/` pronto para uso.  

---

## ⚙️ Ambiente Virtual e Dependências  

Este projeto utiliza um ambiente virtual Python para garantir que as dependências sejam isoladas e que o pipeline rode de forma reprodutível.  

### 📜 Criação do Ambiente Virtual:  

```bash
# Crie o ambiente virtual na raiz do projeto
python -m venv .venv

# Ative o ambiente virtual
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate       # Windows
```

### 📦 Instalação das Dependências:  

```bash
pip install -r requirements.txt
```

### 🔥 Principais bibliotecas utilizadas:  

| Biblioteca     | Finalidade                                                
|----------------|-----------------------------------------------------------|
| **pandas**     | Manipulação de dados                                      |
| **numpy**      | Operações numéricas e vetorização                         |
| **scikit-learn**| Modelagem, métricas e algoritmos de machine learning     |
| **xgboost**    | Algoritmo de boosting otimizado                           |
| **duckdb**     | Banco de dados analítico local, eficiente e leve          |
| **matplotlib** | Visualização de dados                                     |
| **seaborn**    | Visualização estatística                                  |
| **jupyterlab** | Ambiente interativo para notebooks                        |

### 📚 Gerenciamento de Dependências:  

Se você quiser adicionar uma nova biblioteca durante o desenvolvimento, faça:  

```bash
pip install nome-da-biblioteca
```

E depois atualize o arquivo `requirements.txt`:  

```bash
pip freeze > requirements.txt
```

---

## 🚧 Como Executar  

### ▶️ Passos  

```bash
# Clone o repositório
git clone https://github.com/smalldatalabbr/codeagainstfraud.git

# Acesse a pasta do projeto
cd codeagainstfraud

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate       # Windows

# Instale as dependências
pip install -r requirements.txt

# Criação do banco DuckDB (se necessário)
python pipelines/data_preparation.py
```

---

## 📊 Notebooks Disponíveis  
- `01_eda.ipynb` → Análise exploratória inicial (em andamento).  
- `02_feature_eng.ipynb` → Feature Engineering (estrutura criada).  
- `03_modeling.ipynb` → Modelagem supervisionada (estrutura criada).  
- `04_evaluation.ipynb` → Avaliação dos modelos (estrutura criada).  

---

## 🏗️ Status Atual  
- ✅ Estrutura de projeto criada  
- ✅ Pipeline de Data Preparation implementado e validado  
- ✅ DuckDB gerado e incluso no repositório  
- ✅ Notebook de EDA iniciado e validado  
- 🚧 Próximos passos: Feature Engineering, Modelagem e Avaliação  

---

## 🧠 Autor  
**Jhonathan Domingues**  
Criador do Small Data Lab e Cientista de Dados em Transição  

[🔗 LinkedIn](https://www.linkedin.com/in/jhonathandomingues | [🌐 Small Data Lab](https://smalldatalab.com.br)  

---

## 🛑 Disclaimer  
Este projeto é uma **demonstração técnica**, sem qualquer vínculo com instituições financeiras, empresas ou uso comercial.  
Os dados utilizados são públicos, anonimizados e têm como finalidade **o desenvolvimento de competências, aprendizado e demonstração de soluções técnicas aplicadas à detecção de fraudes.**  

---

## 📜 Licença  
Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
