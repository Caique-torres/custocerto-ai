import pandas as pd
import os

# ==========================================
# CAMINHOS DO PROJETO
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")

ARQUIVO = os.path.join(
    DATA_DIR,
    "transacoes.csv"
)

# ==========================================
# PADRÃO DAS COLUNAS
# ==========================================

COLUNAS = [
    "data",
    "descricao",
    "categoria",
    "tipo",
    "valor"
]


# ==========================================
# CARREGAR DADOS
# ==========================================

def carregar_dados():

    os.makedirs(DATA_DIR, exist_ok=True)

    if os.path.exists(ARQUIVO):

        try:
            df = pd.read_csv(ARQUIVO)

            # Compatibilidade com arquivos antigos
            df.columns = [
                str(coluna).strip().lower()
                for coluna in df.columns
            ]

            renomear = {
                "descrição": "descricao",
                "data": "data",
                "categoria": "categoria",
                "tipo": "tipo",
                "valor": "valor"
            }

            df = df.rename(columns=renomear)

            # Garantir todas as colunas
            for coluna in COLUNAS:
                if coluna not in df.columns:
                    df[coluna] = None

            df = df[COLUNAS]

            # Converter valores
            df["valor"] = pd.to_numeric(
                df["valor"],
                errors="coerce"
            ).fillna(0)

            # Padronizar tipo
            df["tipo"] = (
                df["tipo"]
                .astype(str)
                .str.strip()
                .str.capitalize()
            )

            return df

        except Exception as erro:

            raise RuntimeError(
                f"Erro ao carregar transações: {erro}"
            )

    # Criar arquivo vazio
    df = pd.DataFrame(columns=COLUNAS)

    salvar_dados(df)

    return df


# ==========================================
# SALVAR DADOS
# ==========================================

def salvar_dados(df):

    os.makedirs(DATA_DIR, exist_ok=True)

    df = df.copy()

    df = df.reindex(columns=COLUNAS)

    df.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# ==========================================
# ADICIONAR TRANSAÇÃO
# ==========================================

def adicionar_transacao(
    data,
    descricao,
    categoria,
    tipo,
    valor
):

    if not descricao or not str(descricao).strip():
        raise ValueError("Informe uma descrição.")

    if not categoria or not str(categoria).strip():
        raise ValueError("Informe uma categoria.")

    tipo = str(tipo).strip().capitalize()

    if tipo not in ["Receita", "Despesa"]:
        raise ValueError("Tipo de transação inválido.")

    valor = float(valor)

    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    df = carregar_dados()

    nova = pd.DataFrame([{
        "data": str(data),
        "descricao": str(descricao).strip(),
        "categoria": str(categoria).strip(),
        "tipo": tipo,
        "valor": valor
    }])

    df = pd.concat(
        [df, nova],
        ignore_index=True
    )

    salvar_dados(df)

    return df
