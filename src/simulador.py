
def simular_meta(meta, saldo_atual, meses):
    if meta <= 0 or meses <= 0:
        raise ValueError("Meta e prazo devem ser positivos.")

    falta = max(0, meta - saldo_atual)
    mensal = falta / meses

    return {
        "meta": meta,
        "saldo_atual": saldo_atual,
        "valor_restante": falta,
        "economia_mensal": mensal,
        "meses": meses
    }

def simular_reducao_despesas(despesas, percentual):
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual deve estar entre 0 e 100.")

    economia = despesas * (percentual / 100)

    return {
        "despesas_atuais": despesas,
        "economia": economia,
        "novas_despesas": despesas - economia
    }
