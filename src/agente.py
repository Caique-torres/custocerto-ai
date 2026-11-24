import os
import unicodedata

# ==========================================
# IMPORTAÇÃO DA ANÁLISE FINANCEIRA
# ==========================================

try:
    from .analise import (
        resumo_financeiro,
        gastos_por_categoria,
        maior_despesa
    )
except ImportError:
    from analise import (
        resumo_financeiro,
        gastos_por_categoria,
        maior_despesa
    )


# ==========================================
# CONFIGURAÇÕES
# ==========================================

def normalizar(texto):
    texto = str(texto).lower()

    texto = unicodedata.normalize(
        "NFKD", texto
    )

    return "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    )


def formatar(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


# ==========================================
# RESPOSTAS BASEADAS EM REGRAS
# ==========================================

def responder_python(pergunta, df):

    pergunta = normalizar(pergunta)

    resumo = resumo_financeiro(df)
    gastos = gastos_por_categoria(df)

    # Saldo
    if "saldo" in pergunta:
        return (
            f"Seu saldo registrado é "
            f"{formatar(resumo['saldo'])}."
        )

    # Receitas
    if "receita" in pergunta or "renda" in pergunta:
        return (
            f"Suas receitas registradas totalizam "
            f"{formatar(resumo['receitas'])}."
        )

    # Consulta por categoria
    categorias = {
        "alimentacao": "Alimentação",
        "transporte": "Transporte",
        "moradia": "Moradia",
        "saude": "Saúde",
        "educacao": "Educação",
        "lazer": "Lazer",
        "contas domesticas": "Contas domésticas",
        "outros": "Outros"
    }

    for chave, categoria in categorias.items():

        if chave in pergunta:

            valor = float(
                gastos.get(categoria, 0)
            )

            return (
                f"Seus gastos com {categoria.lower()} "
                f"são de {formatar(valor)}."
            )

    # Maior categoria de despesas
    if "maior" in pergunta or "gastando mais" in pergunta:

        categoria, valor = maior_despesa(df)

        if categoria is None:
            return "Você ainda não possui despesas cadastradas."

        return (
            f"Sua maior categoria de gastos é "
            f"{categoria}, com {formatar(valor)}."
        )

    # Percentual de gastos
    if "percentual" in pergunta or "porcentagem" in pergunta:

        receitas = resumo["receitas"]
        despesas = resumo["despesas"]

        if receitas <= 0:
            return "Não existem receitas suficientes para calcular o percentual."

        percentual = despesas / receitas * 100

        return (
            f"Você utilizou {percentual:.1f}% "
            f"das suas receitas com despesas."
        )

    # Despesas totais
    if "despesa" in pergunta or "gasto" in pergunta:

        return (
            f"Suas despesas registradas totalizam "
            f"{formatar(resumo['despesas'])}."
        )

    # Economia
    if "economia" in pergunta or "economizar" in pergunta:

        return (
            f"Seu saldo registrado é {formatar(resumo['saldo'])}. "
            "Você pode analisar suas categorias de gastos "
            "para identificar oportunidades de economia."
        )

    # Orçamento
    if "orcamento" in pergunta or "limite" in pergunta:

        return (
            "Posso analisar seus gastos por categoria. "
            "Consulte as informações de orçamento no Dashboard."
        )

    return (
        "Sou o CustoCerto AI! 🤖\n\n"
        "Posso ajudar com:\n"
        "- Saldo disponível\n"
        "- Receitas e renda\n"
        "- Despesas e gastos\n"
        "- Alimentação\n"
        "- Transporte\n"
        "- Moradia\n"
        "- Maior categoria de gastos\n"
        "- Percentual de despesas\n"
        "- Economia financeira"
    )


# ==========================================
# CONTEXTO FINANCEIRO PARA GEMINI
# ==========================================

def criar_contexto(df):

    resumo = resumo_financeiro(df)
    gastos = gastos_por_categoria(df)

    categorias = "\n".join(
        [
            f"- {categoria}: {formatar(valor)}"
            for categoria, valor in gastos.items()
        ]
    )

    return f"""
Você é o CustoCerto AI, um assistente especializado
em organização e educação financeira pessoal.

Responda sempre em português brasileiro.

DADOS FINANCEIROS REGISTRADOS:

Receitas: {formatar(resumo['receitas'])}
Despesas: {formatar(resumo['despesas'])}
Saldo: {formatar(resumo['saldo'])}

DESPESAS POR CATEGORIA:

{categorias}

INSTRUÇÕES:

1. Utilize os dados fornecidos para responder.
2. Não invente transações ou valores.
3. Explique os resultados de maneira simples.
4. Sugira formas responsáveis de organizar as finanças.
5. Não prometa ganhos financeiros.
6. Diferencie saldo registrado de dinheiro efetivamente disponível.
7. Quando não houver dados suficientes, informe isso.
8. Apresente valores em reais (R$).
9. Não confunda receitas com despesas.

Seja amigável, profissional e objetivo.
"""


# ==========================================
# INTEGRAÇÃO COM GEMINI
# ==========================================

def responder_gemini(pergunta, df):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    try:

        from google import genai

        client = genai.Client(
            api_key=api_key
        )

        contexto = criar_contexto(df)

        prompt = f"""
{contexto}

PERGUNTA DO CLIENTE:

{pergunta}

Responda considerando os dados financeiros apresentados.
"""

        resposta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if resposta.text:
            return resposta.text

        return None

    except Exception:
        return None


# ==========================================
# FUNÇÃO PRINCIPAL DO AGENTE
# ==========================================

def responder(pergunta, df):

    if not pergunta or not str(pergunta).strip():
        return "Digite uma pergunta para iniciar a conversa."

    # Primeiro verifica se a IA generativa está disponível
    resposta_ia = responder_gemini(
        pergunta,
        df
    )

    if resposta_ia:
        return resposta_ia

    # Se Gemini não estiver disponível,
    # utiliza o assistente baseado em Python
    return responder_python(
        pergunta,
        df
    )
