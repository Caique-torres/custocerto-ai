
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.abspath(__file__))
)

from memoria import carregar_dados, adicionar_transacao
from analise import resumo_financeiro, gastos_por_categoria
from simulador import simular_meta, simular_reducao_despesas
from agente import responder

st.set_page_config(
    page_title="CustoCerto AI",
    page_icon="💰",
    layout="wide"
)

st.title("💰 CustoCerto AI")
st.caption("Inteligência financeira ao seu alcance")

pagina = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Lançamentos",
        "Análise Financeira",
        "Simulador",
        "Assistente AI"
    ]
)

df = carregar_dados()
resumo = resumo_financeiro(df)

if pagina == "Dashboard":

    st.header("Dashboard Financeiro")

    c1, c2, c3 = st.columns(3)

    c1.metric("Receitas", f"R$ {resumo['receitas']:,.2f}")
    c2.metric("Despesas", f"R$ {resumo['despesas']:,.2f}")
    c3.metric("Saldo", f"R$ {resumo['saldo']:,.2f}")

    st.divider()

    gastos = gastos_por_categoria(df)

    if not gastos.empty:
        fig = px.pie(
            values=gastos.values,
            names=gastos.index,
            hole=0.5,
            title="Distribuição das despesas"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df, use_container_width=True)

elif pagina == "Lançamentos":

    st.header("Novo lançamento")

    with st.form("lancamento"):

        data = st.date_input("Data")
        descricao = st.text_input("Descrição")

        tipo = st.selectbox(
            "Tipo",
            ["Receita", "Despesa"]
        )

        categoria = st.text_input("Categoria")

        valor = st.number_input(
            "Valor",
            min_value=0.01,
            step=10.0
        )

        enviar = st.form_submit_button("Salvar")

        if enviar:

            if not descricao.strip() or not categoria.strip():
                st.error("Preencha a descrição e a categoria.")
            else:
                adicionar_transacao(
                    data,
                    descricao,
                    categoria,
                    tipo,
                    valor
                )

                st.success("Lançamento salvo!")
                st.rerun()

elif pagina == "Análise Financeira":

    st.header("Análise Financeira")

    gastos = gastos_por_categoria(df)

    if not gastos.empty:

        st.subheader("Gastos por categoria")

        fig = px.bar(
            x=gastos.index,
            y=gastos.values,
            labels={
                "x": "Categoria",
                "y": "Valor (R$)"
            }
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Cadastre despesas para visualizar a análise.")

elif pagina == "Simulador":

    st.header("Simulador de Economia")

    meta = st.number_input(
        "Meta financeira (R$)",
        min_value=1.0,
        value=5000.0
    )

    meses = st.number_input(
        "Prazo em meses",
        min_value=1,
        value=12
    )

    if st.button("Simular meta"):

        resultado = simular_meta(
            meta,
            resumo["saldo"],
            meses
        )

        st.metric(
            "Economia mensal necessária",
            f"R$ {resultado['economia_mensal']:,.2f}"
        )

        st.write(
            f"Valor restante: R$ {resultado['valor_restante']:,.2f}"
        )

    st.divider()

    percentual = st.slider(
        "Redução de despesas (%)",
        0, 100, 10
    )

    if st.button("Simular redução"):

        resultado = simular_reducao_despesas(
            resumo["despesas"],
            percentual
        )

        st.metric(
            "Economia estimada",
            f"R$ {resultado['economia']:,.2f}"
        )

        st.write(
            f"Novas despesas: R$ {resultado['novas_despesas']:,.2f}"
        )

elif pagina == "Assistente AI":

    st.header("🤖 Assistente Financeiro")

    if "historico" not in st.session_state:
        st.session_state.historico = []

    for mensagem in st.session_state.historico:
        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

    pergunta = st.chat_input("Pergunte sobre suas finanças...")

    if pergunta:

        st.session_state.historico.append({
            "role": "user",
            "content": pergunta
        })

        resposta = responder(pergunta, df)

        st.session_state.historico.append({
            "role": "assistant",
            "content": resposta
        })

        st.rerun()
