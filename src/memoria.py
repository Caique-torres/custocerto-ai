
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
ARQUIVO = os.path.join(DATA_DIR, "transacoes.csv")

COLUNAS = ["Data", "Descrição", "Categoria", "Tipo", "Valor"]

def carregar_dados():
    os.makedirs(DATA_DIR, exist_ok=True)

    if os.path.exists(ARQUIVO):
        return pd.read_csv(ARQUIVO)

    df = pd.DataFrame(columns=COLUNAS)
    df.to_csv(ARQUIVO, index=False)
    return df

def salvar_dados(df):
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(ARQUIVO, index=False)

def adicionar_transacao(data, descricao, categoria, tipo, valor):
    df = carregar_dados()

    nova = pd.DataFrame([{
        "Data": str(data),
        "Descrição": descricao,
        "Categoria": categoria,
        "Tipo": tipo,
        "Valor": float(valor)
    }])

    df = pd.concat([df, nova], ignore_index=True)
    salvar_dados(df)

    return df
