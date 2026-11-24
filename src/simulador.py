# ==========================================
# CUSTOCERTO AI - SIMULADOR FINANCEIRO
# ==========================================


# ==========================================
# SIMULADOR DE META FINANCEIRA
# ==========================================

def simular_meta(meta, saldo_atual, meses):

    meta = float(meta)
    saldo_atual = float(saldo_atual)
    meses = int(meses)

    if meta <= 0:
        raise ValueError(
            "A meta financeira deve ser maior que zero."
        )

    if meses <= 0:
        raise ValueError(
            "O prazo deve ser maior que zero."
        )

    # Valor que falta para alcançar a meta
    falta = max(0, meta - max(0, saldo_atual))

    # Economia necessária por mês
    mensal = falta / meses

    return {
        "meta": meta,
        "saldo_atual": saldo_atual,
        "valor_restante": falta,
        "economia_mensal": mensal,
        "meses": meses,
        "meta_alcancada": falta == 0
    }


# ==========================================
# SIMULADOR DE REDUÇÃO DE DESPESAS
# ==========================================

def simular_reducao_despesas(despesas, percentual):

    despesas = float(despesas)
    percentual = float(percentual)

    if despesas < 0:
        raise ValueError(
            "As despesas não podem ser negativas."
        )

    if percentual < 0 or percentual > 100:
        raise ValueError(
            "O percentual deve estar entre 0 e 100."
        )

    # Cálculo da economia
    economia = despesas * (percentual / 100)

    # Novas despesas após a redução
    novas_despesas = despesas - economia

    return {
        "despesas_atuais": despesas,
        "percentual_reducao": percentual,
        "economia": economia,
        "novas_despesas": novas_despesas
    }


# ==========================================
# SIMULADOR DE ECONOMIA MENSAL
# ==========================================

def simular_economia_mensal(receitas, despesas, percentual):

    receitas = float(receitas)
    despesas = float(despesas)
    percentual = float(percentual)

    if receitas < 0 or despesas < 0:
        raise ValueError(
            "Receitas e despesas não podem ser negativas."
        )

    if percentual < 0 or percentual > 100:
        raise ValueError(
            "O percentual deve estar entre 0 e 100."
        )

    economia = despesas * (percentual / 100)

    novas_despesas = despesas - economia

    novo_saldo = receitas - novas_despesas

    return {
        "receitas": receitas,
        "despesas_atuais": despesas,
        "economia": economia,
        "novas_despesas": novas_despesas,
        "saldo_atual": receitas - despesas,
        "novo_saldo": novo_saldo
    }


# ==========================================
# SIMULADOR DE META COM APORTES
# ==========================================

def calcular_prazo_meta(meta, economia_mensal, saldo_atual=0):

    meta = float(meta)
    economia_mensal = float(economia_mensal)
    saldo_atual = float(saldo_atual)

    if meta <= 0:
        raise ValueError(
            "A meta deve ser maior que zero."
        )

    if economia_mensal <= 0:
        raise ValueError(
            "A economia mensal deve ser maior que zero."
        )

    restante = max(
        0,
        meta - max(0, saldo_atual)
    )

    meses = (
        0 if restante == 0
        else int((restante + economia_mensal - 1e-9)
                 // economia_mensal)
    )

    return {
        "meta": meta,
        "saldo_atual": saldo_atual,
        "valor_restante": restante,
        "economia_mensal": economia_mensal,
        "meses_necessarios": meses
    }
