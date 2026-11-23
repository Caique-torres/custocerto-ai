from google import genai
from config import obter_api_key, GEMINI_MODEL


def resposta_agente(pergunta, contexto=""):
    try:
        client = genai.Client(
            api_key=obter_api_key()
        )

        prompt = f"""
Você é o CustoCerto AI, um assistente
especializado em educação financeira.

Suas responsabilidades:
- Analisar receitas e despesas.
- Identificar gastos excessivos.
- Sugerir formas de economizar.
- Ajudar a organizar o orçamento.
- Explicar conceitos financeiros.
- Ajudar a estabelecer metas.

Responda sempre em português brasileiro.
Seja claro, objetivo e profissional.

CONTEXTO FINANCEIRO:
{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}

Forneça uma resposta útil e baseada nos
dados disponíveis.
Não invente informações financeiras.
"""

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        if not response.text:
            return "O Gemini não retornou uma resposta."

        return response.text

    except Exception as erro:
        return (
            f"Erro na integração com Gemini: "
            f"{type(erro).__name__}: {erro}"
        )


def consultar_gemini(pergunta, contexto=""):
    return resposta_agente(pergunta, contexto)
