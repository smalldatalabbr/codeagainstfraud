"""
🚀 data_preparation.py
------------------------------------
Este script contém funções responsáveis pela preparação dos dados brutos,
incluindo carregamento, limpeza, transformação inicial e criação do banco DuckDB.

Papel no pipeline:
- Ingestão do dataset CSV.
- Conversão para DuckDB.
- Processamento inicial (remoção de duplicados, checagem de dados, etc.).
"""

import os
import pandas as pd
import duckdb

def create_duckdb_database(csv_path, db_path):
    # Verifica se o banco já existe
    if os.path.exists(db_path):
        print(f"Database {db_path} já existe. Pulando criação.")
        return

    print(f"Criando database {db_path} a partir do CSV {csv_path}...")

    # Carrega CSV
    df = pd.read_csv(csv_path)

    # Cria conexão DuckDB
    con = duckdb.connect(db_path)

    # Cria a tabela
    con.execute("CREATE TABLE creditcard AS SELECT * FROM df")

    # Fecha
    con.close()

    print("Database criado com sucesso.")

if __name__ == "__main__":
    CSV_PATH = 'data/raw/creditcard.csv'
    DB_PATH = 'data/interim/fraud_data.duckdb'

    create_duckdb_database(CSV_PATH, DB_PATH)

