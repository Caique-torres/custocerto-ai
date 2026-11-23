
#  Código da Aplicação — CustoCerto AI

Esta pasta contém os códigos-fonte do **CustoCerto AI**, um agente inteligente desenvolvido em Python para auxiliar no controle, análise e planejamento de custos mensais.

A aplicação utiliza processamento de dados financeiros, cálculos automatizados e IA Generativa para oferecer informações sobre receitas, despesas e orçamento mensal.

##  Estrutura do Projeto

```text
📁 src/
│   ├── app.py          # Aplicação principal com interface Streamlit
│   ├── agente.py       # Lógica e comportamento do agente de IA
│   ├── analise.py      # Análise financeira e geração de indicadores
│   ├── simulador.py    # Simulação de metas e planejamento financeiro
│   └── memoria.py      # Armazenamento e gerenciamento dos dados financeiros
```

##  Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento da aplicação |
| Streamlit | Interface interativa |
| Pandas | Manipulação de dados financeiros |
| Plotly | Visualização de gráficos |
| Google Gemini | Inteligência Artificial Generativa |
| JSON e CSV | Armazenamento dos dados |

##  Funcionalidades

- Análise de receitas e despesas mensais.
- Cálculo de saldo financeiro.
- Identificação das categorias com maiores gastos.
- Comparação de despesas com o orçamento mensal.
- Simulação de economia e metas financeiras.
- Assistente virtual para dúvidas sobre finanças pessoais.

##  Dependências — requirements.txt

```text
streamlit
pandas
plotly
google-genai
python-dotenv
```

##  Como Executar a Aplicação

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar a chave da API Gemini

A chave deve ser armazenada em variável de ambiente ou segredo local, nunca diretamente no código ou no GitHub.

Exemplo:

```text
GEMINI_API_KEY=sua_chave_api
```

### 3. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta no navegador, permitindo interagir com o CustoCerto AI.

##  Integração com a Base de Conhecimento

O agente utiliza os arquivos armazenados na pasta `data/`:

- `transacoes.csv`
- `historico_atendimento.csv`
- `perfil_financeiro.json`
- `orcamento_mensal.json`

Esses arquivos fornecem informações para contextualizar as análises e respostas do agente.

##  Segurança

- Não armazenar chaves de API diretamente no código.
- Utilizar dados fictícios para demonstrações.
- Não compartilhar informações financeiras sensíveis.
- Basear os cálculos nos dados disponíveis.
- Informar quando não houver dados suficientes para responder.

##  Status do Desenvolvimento

O projeto está em desenvolvimento, com protótipo em Python no Google Colab e estrutura preparada para execução por meio do Streamlit.

A integração com a Gemini API será utilizada para ampliar a interpretação de perguntas em linguagem natural e gerar respostas contextualizadas.

---

**Projeto:** CustoCerto AI — Agente Inteligente de Custos Mensais.

