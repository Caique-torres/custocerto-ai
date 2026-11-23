import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"


def obter_api_key():
    # Primeiro tenta variável de ambiente
    chave = os.getenv("GEMINI_API_KEY")

    # Depois tenta os Secrets do Streamlit
    if not chave:
        try:
            chave = st.secrets["GEMINI_API_KEY"]
        except Exception:
            chave = None

    if not chave:
        raise ValueError(
            "GEMINI_API_KEY não configurada. "
            "Configure a chave no arquivo .env ou nos Secrets."
        )

    return chave
