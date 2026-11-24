import pandas as pd

# ==========================================
# PADRONIZAÇÃO DOS DADOS
# ==========================================

def preparar_dados(df):

    df = df.copy()

    df.columns = [
        str(coluna).strip().lower()
        for coluna in df.columns
    ]

    # Compatibilidade com nomes antigos
    df = df.rename(columns={
        "descrição": "descricao"
    })

    colunas = [
        "data",
        "descricao",
        "categoria",
        "tipo",
        "valor"
    ]

    for coluna in colunas:
        if coluna not in df.columns:
            df[coluna] = None

    df["tipo"] = (
        df["tipo"]
        .astype(str)
        .str.strip()
        .str.capitalize()
    )

    df["valor"] = pd.to_numeric(
        df["valor"],
        errors="coerce"
    ).fillna(0)

    return df


# ==========================================
# RESUMO FINANCEIRO
# ==========================================

def resumo_financeiro(df):

    df = preparar_dados(df)

    receitas = df.loc[
        df["tipo"] == "Receita",
        "valor"
    ].sum()

    despesas = df.loc[
        df["tipo"] == "Despesa",
        "valor"
    ].sum()

    saldo = receitas - despesas

    return {
        "receitas": float(receitas),
        "despesas": float(despesas),
        "saldo": float(saldo)
    }


# ==========================================
# GASTOS POR CATEGORIA
# ==========================================

def gastos_por_categoria(df):

    df = preparar_dados(df)

    despesas = df[
        df["tipo"] == "Despesa"
    ]

    return (
        despesas
        .groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )


# ==========================================
# MAIOR DESPESA
# ==========================================

def maior_despesa(df):

    gastos = gastos_por_categoria(df)

    if gastos.empty:
        return None, 0

    return (
        gastos.idxmax(),
        float(gastos.max())
    )


# ==========================================
# PERCENTUAL DE GASTOS
# ==========================================

def percentual_gastos(df):

    resumo = resumo_financeiro(df)

    receitas = resumo["receitas"]
    despesas = resumo["despesas"]

    if receitas <= 0:
        return 0

    return round(
        despesas / receitas * 100,
        2
    )


# ==========================================
# SALDO FINANCEIRO
# ==========================================

def calcular_saldo(df):

    resumo = resumo_financeiro(df)

    return resumo["saldo"]


# ==========================================
# ANÁLISE POR CATEGORIA
# ==========================================

def analisar_categoria(df, categoria):

    gastos = gastos_por_categoria(df)

    valor = float(
        gastos.get(categoria, 0)
    )

    return {
        "categoria": categoria,
        "gasto": valor
    }


# ==========================================
# RESUMO INTELIGENTE
# ==========================================

def gerar_resumo(df):

    resumo = resumo_financeiro(df)

    categoria, maior_valor = maior_despesa(df)

    percentual = percentual_gastos(df)

    resultado = f"""
### 📊 Resumo Financeiro

- Receitas: R$ {resumo['receitas']:.2f}
- Despesas: R$ {resumo['despesas']:.2f}
- Saldo: R$ {resumo['saldo']:.2f}
- Percentual da renda utilizado: {percentual:.2f}%
"""

    if categoria:

        resultado += f"""

### ⚠️ Maior categoria de despesas

- Categoria: {categoria}
- Total gasto: R$ {maior_valor:.2f}
"""

    return resultado
