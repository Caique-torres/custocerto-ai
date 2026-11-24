import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ==========================================
# CONFIGURAÇÃO
# ==========================================

st.set_page_config(
    page_title="CustoCerto AI",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #F4F7FB;
}
h1, h2, h3 {
    color: #17324D;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# BANCO DE DADOS DA SESSÃO
# ==========================================

COLUNAS = [
    "data", "descricao", "categoria", "tipo", "valor"
]

if "transacoes" not in st.session_state:

    dados = [
        ["2026-11-01", "Salário", "Renda", "Receita", 4500],
        ["2026-11-02", "Aluguel", "Moradia", "Despesa", 1200],
        ["2026-11-03", "Supermercado", "Alimentação", "Despesa", 350],
        ["2026-11-04", "Conta de luz", "Contas domésticas", "Despesa", 150],
        ["2026-11-05", "Combustível", "Transporte", "Despesa", 180],
        ["2026-11-06", "Internet", "Contas domésticas", "Despesa", 100],
        ["2026-11-07", "Restaurante", "Alimentação", "Despesa", 120],
        ["2026-11-08", "Academia", "Saúde", "Despesa", 100],
        ["2026-11-09", "Cinema", "Lazer", "Despesa", 60],
        ["2026-11-10", "Curso online", "Educação", "Despesa", 150],
    ]

    st.session_state.transacoes = pd.DataFrame(
        dados, columns=COLUNAS
    )

df = st.session_state.transacoes.copy()

# ==========================================
# FUNÇÕES FINANCEIRAS
# ==========================================

def resumo_financeiro(df):

    receitas = df.loc[
        df["tipo"] == "Receita", "valor"
    ].sum()

    despesas = df.loc[
        df["tipo"] == "Despesa", "valor"
    ].sum()

    return {
        "receitas": receitas,
        "despesas": despesas,
        "saldo": receitas - despesas
    }


def gastos_por_categoria(df):

    despesas = df[
        df["tipo"] == "Despesa"
    ]

    return despesas.groupby(
        "categoria"
    )["valor"].sum().sort_values(
        ascending=False
    )


def responder(pergunta, df):

    pergunta = pergunta.lower()

    resumo = resumo_financeiro(df)
    gastos = gastos_por_categoria(df)

    if "saldo" in pergunta:
        return f"Seu saldo registrado é R$ {resumo['saldo']:,.2f}."

    if "receita" in pergunta or "renda" in pergunta:
        return f"Suas receitas são R$ {resumo['receitas']:,.2f}."

    if "despesa" in pergunta or "gastei" in pergunta:
        return f"Suas despesas são R$ {resumo['despesas']:,.2f}."

    if "alimentação" in pergunta or "alimentacao" in pergunta:
        return f"Você gastou R$ {gastos.get('Alimentação', 0):,.2f} com alimentação."

    if "transporte" in pergunta:
        return f"Você gastou R$ {gastos.get('Transporte', 0):,.2f} com transporte."

    if "moradia" in pergunta:
        return f"Você gastou R$ {gastos.get('Moradia', 0):,.2f} com moradia."

    if "maior" in pergunta:
        if gastos.empty:
            return "Não existem despesas cadastradas."
        return f"Sua maior categoria é {gastos.idxmax()}, com R$ {gastos.max():,.2f}."

    if "econom" in pergunta:
        return f"Seu saldo atual é R$ {resumo['saldo']:,.2f}. Analise suas categorias para encontrar oportunidades de economia."

    return (
        "Sou o CustoCerto AI! Posso ajudar com saldo, "
        "receitas, despesas, alimentação, transporte, "
        "moradia e metas de economia."
    )


# ==========================================
# CABEÇALHO
# ==========================================

st.title("💰 CustoCerto AI")
st.caption("Seu assistente inteligente de organização financeira")

# ==========================================
# MENU
# ==========================================

pagina = st.sidebar.radio(
    "MENU PRINCIPAL",
    [
        "Dashboard",
        "Lançamentos",
        "Análise Financeira",
        "Simulador",
        "Assistente AI"
    ]
)

resumo = resumo_financeiro(df)

# ==========================================
# DASHBOARD
# ==========================================

if pagina == "Dashboard":

    st.header("📊 Dashboard Financeiro")

    c1, c2, c3 = st.columns(3)

    c1.metric("Receitas", f"R$ {resumo['receitas']:,.2f}")
    c2.metric("Despesas", f"R$ {resumo['despesas']:,.2f}")
    c3.metric("Saldo", f"R$ {resumo['saldo']:,.2f}")

    gastos = gastos_por_categoria(df)

    if not gastos.empty:

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribuição dos gastos")

            fig = px.pie(
                values=gastos.values,
                names=gastos.index,
                hole=0.5
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Gastos por categoria")

            fig = px.bar(
                x=gastos.index,
                y=gastos.values,
                labels={"x": "Categoria", "y": "Valor (R$)"}
            )

            st.plotly_chart(fig, use_container_width=True)

    st.subheader("Movimentações financeiras")

    st.dataframe(df, use_container_width=True, hide_index=True)

# ==========================================
# LANÇAMENTOS
# ==========================================

elif pagina == "Lançamentos":

    st.header("💳 Novo lançamento")

    with st.form("novo_lancamento"):

        data = st.date_input("Data")

        descricao = st.text_input("Descrição")

        tipo = st.selectbox(
            "Tipo",
            ["Receita", "Despesa"]
        )

        categoria = st.selectbox(
            "Categoria",
            [
                "Renda",
                "Moradia",
                "Alimentação",
                "Transporte",
                "Saúde",
                "Educação",
                "Lazer",
                "Contas domésticas",
                "Outros"
            ]
        )

        valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            value=100.00
        )

        salvar = st.form_submit_button(
            "Salvar lançamento"
        )

        if salvar:

            if not descricao.strip():
                st.error("Informe a descrição.")

            else:

                novo = pd.DataFrame([{
                    "data": str(data),
                    "descricao": descricao,
                    "categoria": categoria,
                    "tipo": tipo,
                    "valor": valor
                }])

                st.session_state.transacoes = pd.concat(
                    [st.session_state.transacoes, novo],
                    ignore_index=True
                )

                st.success("Lançamento cadastrado!")
                st.rerun()

# ==========================================
# ANÁLISE FINANCEIRA
# ==========================================

elif pagina == "Análise Financeira":

    st.header("📈 Análise Financeira")

    gastos = gastos_por_categoria(df)

    percentual = (
        resumo["despesas"] / resumo["receitas"] * 100
        if resumo["receitas"] > 0 else 0
    )

    st.metric(
        "Percentual da renda utilizado",
        f"{percentual:.1f}%"
    )

    if not gastos.empty:

        fig = px.bar(
            x=gastos.index,
            y=gastos.values,
            text_auto=".2f",
            labels={"x": "Categoria", "y": "Valor (R$)"}
        )

        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(
            gastos.rename("Total gasto"),
            use_container_width=True
        )

# ==========================================
# SIMULADOR
# ==========================================

elif pagina == "Simulador":

    st.header("🎯 Simulador de Economia")

    meta = st.number_input(
        "Sua meta financeira (R$)",
        min_value=1.0,
        value=5000.0
    )

    meses = st.number_input(
        "Prazo em meses",
        min_value=1,
        value=12
    )

    if st.button("Simular meta"):

        falta = max(0, meta - resumo["saldo"])

        mensal = falta / meses

        st.metric(
            "Economia mensal necessária",
            f"R$ {mensal:,.2f}"
        )

        st.write(
            f"Valor restante: R$ {falta:,.2f}"
        )

    st.divider()

    percentual = st.slider(
        "Redução das despesas (%)",
        0, 100, 10
    )

    if st.button("Simular redução"):

        economia = resumo["despesas"] * percentual / 100

        st.metric(
            "Economia estimada",
            f"R$ {economia:,.2f}"
        )

        st.metric(
            "Novas despesas",
            f"R$ {resumo['despesas'] - economia:,.2f}"
        )

# ==========================================
# ASSISTENTE AI
# ==========================================

elif pagina == "Assistente AI":

    st.header("🤖 Assistente Financeiro")

    if "historico" not in st.session_state:
        st.session_state.historico = []

    for mensagem in st.session_state.historico:

        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

    pergunta = st.chat_input(
        "Pergunte sobre suas finanças..."
    )

    if pergunta:

        st.session_state.historico.append({
            "role": "user",
            "content": pergunta
        })

        resposta = responder(
            pergunta,
            df
        )

        st.session_state.historico.append({
            "role": "assistant",
            "content": resposta
        })

        st.rerun()

    if st.button("Limpar conversa"):
        st.session_state.historico = []
        st.rerun()

# ==========================================
# RODAPÉ
# ==========================================

st.sidebar.divider()
st.sidebar.caption("CustoCerto AI © 2026")
st.sidebar.caption("Controle financeiro inteligente")
