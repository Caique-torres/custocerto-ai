import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="CustoCerto AI",
    page_icon="💰",
    layout="wide"
)

# CONFIGURAÇÕES
st.markdown("""
<style>
.stApp {
    background-color: #F5F7FA;
}
[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
}
h1, h2, h3 {
    color: #173B35;
}
</style>
""", unsafe_allow_html=True)

st.title("💰 CustoCerto AI")
st.caption("Seu assistente inteligente de controle financeiro")

CATEGORIAS = [
    "Moradia", "Alimentação", "Transporte",
    "Saúde", "Educação", "Lazer",
    "Contas Domésticas", "Outros"
]

LIMITES_INICIAIS = {
    "Moradia": 1500,
    "Alimentação": 700,
    "Transporte": 350,
    "Saúde": 250,
    "Educação": 200,
    "Lazer": 200,
    "Contas Domésticas": 300,
    "Outros": 300
}

# DADOS INICIAIS DO NOTEBOOK
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame([
        ["2026-11-01", "Salário", "Renda", "Receita", 4500],
        ["2026-11-02", "Aluguel", "Moradia", "Despesa", 1200],
        ["2026-11-03", "Supermercado", "Alimentação", "Despesa", 350],
        ["2026-11-04", "Conta de luz", "Contas Domésticas", "Despesa", 150],
        ["2026-11-05", "Combustível", "Transporte", "Despesa", 180],
        ["2026-11-06", "Internet", "Contas Domésticas", "Despesa", 100],
        ["2026-11-07", "Restaurante", "Alimentação", "Despesa", 120],
        ["2026-11-08", "Academia", "Saúde", "Despesa", 100],
        ["2026-11-09", "Cinema", "Lazer", "Despesa", 60],
        ["2026-11-10", "Curso online", "Educação", "Despesa", 150],
        ["2026-11-11", "Supermercado", "Alimentação", "Despesa", 280],
        ["2026-11-12", "Água", "Contas Domésticas", "Despesa", 80],
        ["2026-11-13", "Aplicativo", "Transporte", "Despesa", 90],
        ["2026-11-14", "Consulta médica", "Saúde", "Despesa", 150],
        ["2026-11-15", "Lanche", "Lazer", "Despesa", 45],
        ["2026-11-16", "Compra pessoal", "Outros", "Despesa", 120],
        ["2026-11-17", "Supermercado", "Alimentação", "Despesa", 250],
        ["2026-11-18", "Manutenção", "Moradia", "Despesa", 200],
        ["2026-11-19", "Combustível", "Transporte", "Despesa", 100],
        ["2026-11-20", "Material de estudo", "Educação", "Despesa", 50],
    ], columns=[
        "Data", "Descrição", "Categoria", "Tipo", "Valor"
    ])

if "limites" not in st.session_state:
    st.session_state.limites = LIMITES_INICIAIS.copy()

if "chat" not in st.session_state:
    st.session_state.chat = []

df = st.session_state.df

# MENU
st.sidebar.title("📊 Menu principal")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Dashboard",
        "Lançamentos",
        "Orçamento",
        "Metas de Economia",
        "Assistente AI"
    ]
)

receitas = df.loc[df["Tipo"] == "Receita", "Valor"].sum()
despesas = df.loc[df["Tipo"] == "Despesa", "Valor"].sum()
saldo = receitas - despesas

# DASHBOARD
if pagina == "Dashboard":

    st.header("Visão geral financeira")

    col1, col2, col3 = st.columns(3)

    col1.metric("💵 Receitas", f"R$ {receitas:,.2f}")
    col2.metric("💸 Despesas", f"R$ {despesas:,.2f}")
    col3.metric("💰 Saldo disponível", f"R$ {saldo:,.2f}")

    st.divider()

    despesas_df = df[df["Tipo"] == "Despesa"]

    gastos = (
        despesas_df.groupby("Categoria")["Valor"]
        .sum()
        .reset_index()
        .sort_values("Valor", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Despesas por categoria")

        if not gastos.empty:
            fig = px.pie(
                gastos,
                names="Categoria",
                values="Valor",
                hole=0.55,
                title="Distribuição dos gastos"
            )
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Comparativo de despesas")

        if not gastos.empty:
            fig = px.bar(
                gastos,
                x="Categoria",
                y="Valor",
                color="Valor",
                title="Gastos por categoria"
            )
            st.plotly_chart(fig, use_container_width=True)

    st.subheader("Últimas movimentações")
    st.dataframe(df.tail(10), use_container_width=True)

    st.download_button(
        "📥 Exportar movimentações CSV",
        df.to_csv(index=False).encode("utf-8-sig"),
        "transacoes.csv",
        "text/csv"
    )

# LANÇAMENTOS
elif pagina == "Lançamentos":

    st.header("📝 Gerenciar lançamentos")

    with st.form("novo_lancamento"):

        data = st.date_input("Data")

        descricao = st.text_input("Descrição")

        tipo = st.selectbox(
            "Tipo de movimentação",
            ["Despesa", "Receita"]
        )

        categoria = st.selectbox(
            "Categoria",
            CATEGORIAS if tipo == "Despesa" else ["Renda", "Outros"]
        )

        valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            step=10.0
        )

        salvar = st.form_submit_button("Adicionar lançamento")

        if salvar:
            novo = pd.DataFrame([{
                "Data": str(data),
                "Descrição": descricao,
                "Categoria": categoria,
                "Tipo": tipo,
                "Valor": valor
            }])

            st.session_state.df = pd.concat(
                [st.session_state.df, novo],
                ignore_index=True
            )

            st.success("Lançamento adicionado!")
            st.rerun()

    st.divider()

    st.subheader("Histórico financeiro")
    st.dataframe(st.session_state.df, use_container_width=True)

    if st.button("Limpar todos os lançamentos"):
        st.session_state.df = st.session_state.df.iloc[0:0]
        st.rerun()

# ORÇAMENTO
elif pagina == "Orçamento":

    st.header("📊 Controle de orçamento")

    gastos = (
        st.session_state.df[
            st.session_state.df["Tipo"] == "Despesa"
        ]
        .groupby("Categoria")["Valor"]
        .sum()
    )

    for categoria, limite in st.session_state.limites.items():

        gasto = gastos.get(categoria, 0)
        percentual = gasto / limite if limite > 0 else 0

        st.subheader(categoria)

        st.write(
            f"Gasto: R$ {gasto:,.2f} | "
            f"Limite: R$ {limite:,.2f}"
        )

        st.progress(min(percentual, 1.0))

        if percentual > 1:
            st.error("🚨 Orçamento ultrapassado!")

        elif percentual >= 0.8:
            st.warning("⚠️ Atenção: próximo do limite!")

        else:
            st.success("✅ Dentro do orçamento")

        novo_limite = st.number_input(
            f"Editar limite de {categoria}",
            min_value=0.0,
            value=float(limite),
            key=f"limite_{categoria}"
        )

        st.session_state.limites[categoria] = novo_limite

        st.divider()

# METAS
elif pagina == "Metas de Economia":

    st.header("🎯 Simulador de economia")

    st.metric("Saldo atual", f"R$ {saldo:,.2f}")

    meta = st.number_input(
        "Qual sua meta financeira? (R$)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    prazo = st.number_input(
        "Prazo em meses",
        min_value=1,
        value=12
    )

    if st.button("Simular economia"):

        falta = max(0, meta - saldo)
        economia_mensal = falta / prazo

        if falta == 0:
            st.success("🎉 Parabéns! Você já alcançou sua meta.")
        else:
            st.info(
                f"Você precisa economizar R$ {falta:,.2f}."
            )

            st.metric(
                "Economia mensal necessária",
                f"R$ {economia_mensal:,.2f}"
            )

# ASSISTENTE AI
elif pagina == "Assistente AI":

    st.header("🤖 Assistente CustoCerto AI")

    st.write(
        "Pergunte sobre suas receitas, despesas, "
        "orçamento e planejamento financeiro."
    )

    def responder(pergunta):

        p = pergunta.lower()

        if "receita" in p or "renda" in p:
            return f"Suas receitas totalizam R$ {receitas:,.2f}."

        elif "saldo" in p:
            return f"Seu saldo disponível é R$ {saldo:,.2f}."

        elif "despesa" in p or "gastei" in p:
            return f"Suas despesas totalizam R$ {despesas:,.2f}."

        elif "maior gasto" in p or "gastando mais" in p:

            gastos = (
                st.session_state.df[
                    st.session_state.df["Tipo"] == "Despesa"
                ].groupby("Categoria")["Valor"].sum()
            )

            if gastos.empty:
                return "Ainda não existem despesas cadastradas."

            return (
                f"Sua maior despesa é {gastos.idxmax()}, "
                f"com R$ {gastos.max():,.2f}."
            )

        elif "alimentação" in p or "alimentacao" in p:
            valor = st.session_state.df[
                (st.session_state.df["Categoria"] == "Alimentação") &
                (st.session_state.df["Tipo"] == "Despesa")
            ]["Valor"].sum()

            return f"Seus gastos com alimentação são R$ {valor:,.2f}."

        elif "transporte" in p:
            valor = st.session_state.df[
                (st.session_state.df["Categoria"] == "Transporte") &
                (st.session_state.df["Tipo"] == "Despesa")
            ]["Valor"].sum()

            return f"Seus gastos com transporte são R$ {valor:,.2f}."

        elif "moradia" in p:
            valor = st.session_state.df[
                (st.session_state.df["Categoria"] == "Moradia") &
                (st.session_state.df["Tipo"] == "Despesa")
            ]["Valor"].sum()

            return f"Seus gastos com moradia são R$ {valor:,.2f}."

        elif "economia" in p or "economizar" in p:
            return (
                f"Seu saldo atual é R$ {saldo:,.2f}. "
                "Defina uma meta na página Metas de Economia."
            )

        return (
            "Posso ajudar com receitas, despesas, saldo, "
            "alimentação, transporte, moradia e economia."
        )

    for mensagem in st.session_state.chat:

        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

    pergunta = st.chat_input("Digite sua pergunta...")

    if pergunta:

        st.session_state.chat.append({
            "role": "user",
            "content": pergunta
        })

        resposta = responder(pergunta)

        st.session_state.chat.append({
            "role": "assistant",
            "content": resposta
        })

        st.rerun()

    if st.button("Limpar conversa"):
        st.session_state.chat = []
        st.rerun()

st.sidebar.divider()
st.sidebar.caption("CustoCerto AI | Controle financeiro inteligente")
