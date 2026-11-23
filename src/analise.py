
import pandas as pd

def resumo_financeiro(df):
    receitas = df.loc[df["Tipo"] == "Receita", "Valor"].sum()
    despesas = df.loc[df["Tipo"] == "Despesa", "Valor"].sum()

    return {
        "receitas": receitas,
        "despesas": despesas,
        "saldo": receitas - despesas
    }

def gastos_por_categoria(df):
    despesas = df[df["Tipo"] == "Despesa"]

    return (
        despesas.groupby("Categoria")["Valor"]
        .sum()
        .sort_values(ascending=False)
    )

def maior_despesa(df):
    gastos = gastos_por_categoria(df)

    if gastos.empty:
        return None, 0

    return gastos.idxmax(), gastos.max()

def percentual_gastos(df):
    resumo = resumo_financeiro(df)

    if resumo["receitas"] == 0:
        return 0

    return resumo["despesas"] / resumo["receitas"] * 100
