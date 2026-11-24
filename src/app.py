
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

# ==========================================
# CONFIGURAÇÃO DOS CAMINHOS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# ==========================================
# IMPORTAÇÃO DOS MÓDULOS SRC
# ==========================================

try:
    from memoria import carregar_dados, adicionar_transacao
    from analise import resumo_financeiro, gastos_por_categoria
    from simulador import simular_meta, simular_reducao_despesas
    from agente import responder

except ImportError as erro:
    st.error(f"Erro ao carregar os módulos: {erro}")
    st.stop()

# ==========================================
# CONFIGURAÇÃO STREAMLIT
# ==========================================

st.set_page_config(
    page_title="CustoCerto AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILO VISUAL
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #F5F7FB;
}

h1, h2, h3 {
    color: #17324D;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #E5EAF0;
}

section[data-testid="stSidebar"] {
    background-color: #102D46;
}

section[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# CABEÇALHO
# ==========================================

st.title("💰 CustoCerto AI")

st.caption(
    "Inteligência financeira ao seu alcance"
)

st.divider()

# ==========================================
# MENU
# ==========================================

pagina = st.sidebar.radio(
    "📌 MENU PRINCIPAL",
    [
        "Dashboard",
        "Lançamentos",
        "Análise Financeira",
        "Simulador",
        "Assistente AI"
    ]
)

st.sidebar.divider()
st.sidebar.caption("CustoCerto AI © 2026")
st.sidebar.caption("Controle financeiro inteligente")

# ==========================================
# CARREGAMENTO DOS DADOS
# ==========================================

try:
    df = carregar_dados()

    resumo = resumo_financeiro(df)

except Exception as erro:
    st.error(f"Erro ao carregar dados financeiros: {erro}")
    st.stop()

# ==========================================
# DASHBOARD
# ==========================================

if pagina == "Dashboard":

    st.header("📊 Dashboard Financeiro")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "💵 Receitas",
        f"R$ {resumo['receitas']:,.2f}"
    )

    c2.metric(
        "💸 Despesas",
        f"R$ {resumo['despesas']:,.2f}"
    )

    c3.metric(
        "💰 Saldo disponível",
        f"R$ {resumo['saldo']:,.2f}"
    )

    st.divider()

    gastos = gastos_por_categoria(df)

    if not gastos.empty:

        st.subheader("Distribuição das despesas")

        fig = px.pie(
            values=gastos.values,
            names=gastos.index,
            hole=0.5,
            title="Gastos por categoria",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Comparativo de despesas")

        grafico = px.bar(
            x=gastos.index,
            y=gastos.values,
            labels={
                "x": "Categoria",
                "y": "Valor em R$"
            },
            color=gastos.values,
            color_continuous_scale="Blues"
        )

        st.plotly_chart(
            grafico,
            use_container_width=True
        )

    else:
        st.info("Ainda não existem despesas cadastradas.")

    st.subheader("Últimas movimentações")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    if st.button("🔄 Atualizar dashboard"):
        st.rerun()

# ==========================================
# LANÇAMENTOS
# ==========================================

elif pagina == "Lançamentos":

    st.header("💳 Novo lançamento")

    st.write(
        "Registre suas receitas e despesas financeiras."
    )

    with st.form("form_lancamento"):

        data = st.date_input(
            "Data",
            value=pd.Timestamp.today().date()
        )

        descricao = st.text_input(
            "Descrição",
            placeholder="Ex: Supermercado"
        )

        tipo = st.selectbox(
            "Tipo de movimentação",
            ["Receita", "Despesa"]
        )

        categorias = [
            "Moradia",
            "Alimentação",
            "Transporte",
            "Saúde",
            "Educação",
            "Lazer",
            "Contas domésticas",
            "Outros"
        ]

        categoria = st.selectbox(
            "Categoria",
            categorias
        )

        valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            value=100.00,
            step=10.00
        )

        enviar = st.form_submit_button(
            "💾 Salvar lançamento",
            use_container_width=True
        )

        if enviar:

            if not descricao.strip():
                st.error("Informe a descrição.")

            else:

                try:

                    adicionar_transacao(
                        data,
                        descricao.strip(),
                        categoria,
                        tipo,
                        valor
                    )

                    st.success(
                        "✅ Lançamento salvo com sucesso!"
                    )

                    st.rerun()

                except Exception as erro:

                    st.error(
                        f"Não foi possível salvar: {erro}"
                    )

# ==========================================
# ANÁLISE FINANCEIRA
# ==========================================

elif pagina == "Análise Financeira":

    st.header("📈 Análise Financeira")

    gastos = gastos_por_categoria(df)

    if not gastos.empty:

        st.subheader("Gastos por categoria")

        fig = px.bar(
            x=gastos.index,
            y=gastos.values,
            text_auto=".2f",
            labels={
                "x": "Categoria",
                "y": "Valor (R$)"
            },
            color=gastos.values,
            color_continuous_scale="Blues"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Resumo das categorias")

        st.dataframe(
            gastos.rename("Total gasto"),
            use_container_width=True
        )

        maior_categoria = gastos.idxmax()

        st.info(
            f"Sua maior categoria de despesas é "
            f"{maior_categoria}, com "
            f"R$ {gastos.max():,.2f}."
        )

    else:

        st.info(
            "Cadastre despesas para visualizar a análise."
        )

# ==========================================
# SIMULADOR
# ==========================================

elif pagina == "Simulador":

    st.header("🎯 Simulador de Economia")

    st.subheader("Planejamento de metas")

    meta = st.number_input(
        "Meta financeira (R$)",
        min_value=1.0,
        value=5000.0,
        step=100.0
    )

    meses = st.number_input(
        "Prazo em meses",
        min_value=1,
        value=12,
        step=1
    )

    if st.button("💰 Simular meta"):

        try:

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
                f"Valor restante: "
                f"R$ {resultado['valor_restante']:,.2f}"
            )

        except Exception as erro:

            st.error(
                f"Erro na simulação: {erro}"
            )

    st.divider()

    st.subheader("Simulação de redução de despesas")

    percentual = st.slider(
        "Redução desejada (%)",
        min_value=0,
        max_value=100,
        value=10
    )

    if st.button("📉 Simular redução"):

        try:

            resultado = simular_reducao_despesas(
                resumo["despesas"],
                percentual
            )

            st.metric(
                "Economia estimada",
                f"R$ {resultado['economia']:,.2f}"
            )

            st.metric(
                "Novas despesas",
                f"R$ {resultado['novas_despesas']:,.2f}"
            )

        except Exception as erro:

            st.error(
                f"Erro na simulação: {erro}"
            )

# ==========================================
# ASSISTENTE AI
# ==========================================

elif pagina == "Assistente AI":

    st.header("🤖 Assistente Financeiro")

    st.write(
        "Pergunte sobre suas receitas, despesas, "
        "orçamento e metas financeiras."
    )

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

        try:

            # Atualizar dados antes da resposta
            df_atual = carregar_dados()

            resposta = responder(
                pergunta,
                df_atual
            )

            if resposta is None:
                resposta = "Não foi possível gerar uma resposta."

        except Exception as erro:

            resposta = (
                f"Não consegui processar sua pergunta: {erro}"
            )

        st.session_state.historico.append({
            "role": "assistant",
            "content": str(resposta)
        })

        st.rerun()

    if st.button("🗑️ Limpar conversa"):

        st.session_state.historico = []
        st.rerun()

# ==========================================
# RODAPÉ
# ==========================================

st.sidebar.divider()

st.sidebar.caption(
    "Desenvolvido para organização financeira."
)
