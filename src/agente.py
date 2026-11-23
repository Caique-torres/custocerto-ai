from analise import resumo_financeiro, gastos_por_categoria

def responder(pergunta, df):
    pergunta = pergunta.lower()
    resumo = resumo_financeiro(df)

    if "saldo" in pergunta:
        return f"Seu saldo atual é R$ {resumo['saldo']:,.2f}."

    if "receita" in pergunta or "renda" in pergunta:
        return f"Suas receitas são R$ {resumo['receitas']:,.2f}."

    if "despesa" in pergunta or "gasto" in pergunta:
        return f"Suas despesas são R$ {resumo['despesas']:,.2f}."

    if "maior" in pergunta:
        gastos = gastos_por_categoria(df)

        if gastos.empty:
            return "Você ainda não possui despesas cadastradas."

        return (
            f"Sua maior categoria de gastos é {gastos.idxmax()}, "
            f"com R$ {gastos.max():,.2f}."
        )

    return (
        "Posso ajudar a analisar seu saldo, receitas, despesas "
        "e maiores categorias de gastos."
    )
