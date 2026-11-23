import os
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from agente import resposta_agente

# Configurações
st.set_page_config(
    page_title="CustoCerto AI",
    page_icon="💰",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ARQUIVO = DATA_DIR / "transacoes.csv"

DATA_DIR.mkdir(exist_ok=True)

COLUNAS = [
    "data",
    "descricao",
    "categoria",
    "tipo",
    "valor"
]


def carregar_dados():
    if ARQUIVO.exists():
        try:
            df = pd.read_csv(ARQUIVO)
            for coluna in COLUNAS:
                if coluna not in df.columns:
                    df[coluna] = None

            df["valor"] = pd.to_numeric(
                df["valor"], errors="coerce"
            ).fillna(0)

            return df[COLUNAS]

        except Exception:
            st.error("Erro ao carregar as transações.")

    return pd.DataFrame(columns=COLUNAS)


def salvar_dados(df):
    df.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


st.title("💰 CustoCerto AI")
st.caption("Seu assistente inteligente de planejamento financeiro.")

df = carregar_dados()

# Menu lateral
pagina = st.sidebar.radio(
    "Navegação",
    [
        "Dashboard",
        "Cadastrar transação",
        "Assistente Gemini",
        "Relatórios"
    ]
)

# DASHBOARD
if pagina == "Dashboard":

    st.header("Visão geral financeira")

    receitas = df.loc[
        df["tipo"] == "Receita", "valor"
    ].sum()

    despesas = df.loc[
        df["tipo"] == "Despesa", "valor"
    ].sum()

    saldo = receitas - despesas

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Receitas",
        f"R$ {receitas:,.2f}"
    )

    col2.metric(
        "Despesas",
        f"R$ {despesas:,.2f}"
    )

    col3.metric(
        "Saldo",
        f"R$ {saldo:,.2f}"
    )

    st.divider()

    if not df.empty:

        despesas_df = df[df["tipo"] == "Despesa"]

        if not despesas_df.empty:
            st.subheader("Despesas por categoria")

            grafico = px.pie(
                despesas_df,
                values="valor",
                names="categoria",
                hole=0.4,
                title="Distribuição dos gastos"
            )

            st.plotly_chart(
                grafico,
                use_container_width=True
            )

        st.subheader("Últimas transações")

        st.dataframe(
            df.sort_values(
                "data", ascending=False
            ),
            use_container_width=True
        )

    else:
        st.info("Cadastre suas primeiras transações.")

# CADASTRO
elif pagina == "Cadastrar transação":

    st.header("Cadastrar nova transação")

    with st.form("form_transacao"):

        data = st.date_input("Data")

        descricao = st.text_input(
            "Descrição"
        )

        categoria = st.selectbox(
            "Categoria",
            [
                "Alimentação",
                "Moradia",
                "Transporte",
                "Saúde",
                "Educação",
                "Lazer",
                "Salário",
                "Investimentos",
                "Outros"
            ]
        )

        tipo = st.selectbox(
            "Tipo",
            ["Receita", "Despesa"]
        )

        valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            step=10.0
        )

        enviar = st.form_submit_button(
            "Salvar transação"
        )

        if enviar:

            if not descricao.strip():
                st.error("Informe uma descrição.")

            else:
                nova = pd.DataFrame([{
                    "data": str(data),
                    "descricao": descricao,
                    "categoria": categoria,
                    "tipo": tipo,
                    "valor": valor
                }])

                df = pd.concat(
                    [df, nova],
                    ignore_index=True
                )

                salvar_dados(df)

                st.success(
                    "Transação cadastrada com sucesso!"
                )

                st.rerun()

# ASSISTENTE GEMINI
elif pagina == "Assistente Gemini":

    st.header("🤖 Assistente financeiro CustoCerto AI")

    st.write(
        "Converse com a inteligência artificial "
        "sobre suas finanças."
    )

    receitas = df.loc[
        df["tipo"] == "Receita", "valor"
    ].sum()

    despesas = df.loc[
        df["tipo"] == "Despesa", "valor"
    ].sum()

    saldo = receitas - despesas

    contexto = f"""
    Receitas totais: R$ {receitas:.2f}
    Despesas totais: R$ {despesas:.2f}
    Saldo atual: R$ {saldo:.2f}

    Transações:
    {df.to_string(index=False)}
    """

    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    for mensagem in st.session_state.mensagens:

        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

    pergunta = st.chat_input(
        "Pergunte sobre suas finanças..."
    )

    if pergunta:

        st.session_state.mensagens.append({
            "role": "user",
            "content": pergunta
        })

        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):

            with st.spinner("Analisando suas finanças..."):

                resposta = resposta_agente(
                    pergunta,
                    contexto
                )

                st.markdown(resposta)

        st.session_state.mensagens.append({
            "role": "assistant",
            "content": resposta
        })

    if st.button("Limpar conversa"):
        st.session_state.mensagens = []
        st.rerun()

# RELATÓRIOS
elif pagina == "Relatórios":

    st.header("📊 Relatórios financeiros")

    if df.empty:
        st.info("Não existem dados para gerar relatórios.")

    else:

        relatorio = df.copy()

        relatorio["data"] = pd.to_datetime(
            relatorio["data"],
            errors="coerce"
        )

        relatorio["mes"] = (
            relatorio["data"].dt.to_period("M").astype(str)
        )

        resumo = relatorio.pivot_table(
            index="mes",
            columns="tipo",
            values="valor",
            aggfunc="sum",
            fill_value=0
        ).reset_index()

        st.subheader("Evolução mensal")

        st.dataframe(
            resumo,
            use_container_width=True
        )

        col1, col2 = st.columns(2)

        with col1:
            if "Receita" in resumo.columns:
                fig = px.bar(
                    resumo,
                    x="mes",
                    y="Receita",
                    title="Receitas mensais"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        with col2:
            if "Despesa" in resumo.columns:
                fig = px.bar(
                    resumo,
                    x="mes",
                    y="Despesa",
                    title="Despesas mensais"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

st.sidebar.divider()
st.sidebar.caption("CustoCerto AI | Versão 1.0")
