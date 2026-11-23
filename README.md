
#  CustoCerto AI — Agente Inteligente de Custos Mensais

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![IA Generativa](https://img.shields.io/badge/IA-Generativa-purple)
![Google Colab](https://img.shields.io/badge/Google-Colab-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![DIO](https://img.shields.io/badge/Desafio-DIO-green)

##  Sobre o Projeto

O **CustoCerto AI** é um agente financeiro inteligente desenvolvido com Python e Inteligência Artificial Generativa, com o objetivo de auxiliar pessoas no controle, análise e previsão de custos mensais.

A solução utiliza dados financeiros para identificar padrões de consumo, detectar possíveis excessos no orçamento e oferecer recomendações personalizadas para melhorar a organização financeira.

Diferentemente de um chatbot tradicional, o agente busca antecipar necessidades, analisar informações e apoiar o usuário na tomada de decisões financeiras mais conscientes.

---

#  1. Caso de Uso

## Problema

Muitas pessoas possuem dificuldades para controlar suas despesas mensais, identificar onde estão gastando mais e planejar seus próximos meses.

## Solução

Desenvolver um agente inteligente capaz de:

- Analisar receitas e despesas.
- Identificar categorias com maiores gastos.
- Detectar aumentos no consumo.
- Prever custos até o final do mês.
- Sugerir oportunidades de economia.
- Responder perguntas sobre a situação financeira.
- Personalizar recomendações conforme o perfil do usuário.

## Objetivos

- Melhorar o controle financeiro mensal.
- Identificar oportunidades de redução de despesas.
- Antecipar possíveis excessos no orçamento.
- Facilitar a interpretação dos dados financeiros.
- Incentivar decisões financeiras conscientes.

---

#  2. Persona e Tom de Voz

| Característica | Definição |
|---|---|
| Nome | CustoCerto AI |
| Perfil | Assistente financeiro digital |
| Personalidade | Consultivo, amigável e objetivo |
| Linguagem | Simples e acessível |
| Comportamento | Proativo e analítico |
| Público-alvo | Pessoas que desejam organizar suas finanças |

### Exemplo de interação

**Usuário:**

Quanto gastei este mês?

**CustoCerto AI:**

Com base nas despesas registradas, você gastou R$ 3.450,00 neste mês.

Identifiquei que alimentação representa uma parcela significativa dos seus gastos. Podemos estabelecer uma meta para reduzir essa despesa no próximo mês.

---

#  3. Arquitetura do Agente

O agente utiliza uma arquitetura que integra processamento de dados, inteligência artificial generativa e cálculos financeiros realizados em Python.

## Fluxo de funcionamento

1. O usuário envia uma pergunta.
2. O agente interpreta a intenção.
3. Os dados financeiros são consultados.
4. O Python realiza os cálculos necessários.
5. A IA interpreta os resultados.
6. O sistema valida as informações.
7. O agente apresenta uma resposta contextualizada.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento do agente |
| Pandas | Manipulação e análise de dados |
| Gradio | Interface de conversação |
| Google Colab | Ambiente de desenvolvimento |
| Gemini API | Inteligência artificial generativa |
| SQLite | Persistência de informações |
| Matplotlib | Visualização de dados |

---

#  4. Segurança e Confiabilidade

Para evitar respostas incorretas e garantir maior confiabilidade:

- Utilizar dados fornecidos pelo usuário.
- Não inventar valores ou transações.
- Executar cálculos financeiros em Python.
- Informar quando não houver dados suficientes.
- Não solicitar senhas ou informações bancárias sigilosas.
- Diferenciar previsões de valores reais.
- Validar os resultados antes de apresentá-los.
- Proteger informações pessoais e financeiras.
- Não compartilhar dados financeiros com terceiros.

---

#  5. Base de Conhecimento

O agente utilizará dados fictícios para simular o comportamento financeiro de um usuário.

Os arquivos estarão organizados na pasta `data/`.

| Arquivo | Formato | Descrição |
|---|---|---|
| `transacoes.csv` | CSV | Histórico de receitas e despesas |
| `historico_atendimento.csv` | CSV | Histórico de conversas |
| `perfil_financeiro.json` | JSON | Perfil e objetivos financeiros |
| `orcamento_mensal.json` | JSON | Limites de gastos por categoria |

## Categorias financeiras

- Moradia
- Alimentação
- Transporte
- Saúde
- Educação
- Lazer
- Contas domésticas
- Outros

---

#  6. Prompts do Agente

Os prompts serão responsáveis por orientar o comportamento da inteligência artificial, garantindo respostas contextualizadas e confiáveis.

## System Prompt

```text
Você é o CustoCerto AI, um agente especializado
em gestão de custos mensais.

Sua função é analisar receitas, despesas e
hábitos de consumo do usuário.

REGRAS:

1. Utilize os dados disponíveis na base de conhecimento.
2. Não invente valores ou transações.
3. Utilize funções Python para realizar cálculos.
4. Identifique oportunidades de economia.
5. Apresente recomendações claras e objetivas.
6. Informe quando não possuir dados suficientes.
7. Considere o contexto das conversas anteriores.
8. Preserve a privacidade do usuário.
9. Diferencie valores reais de previsões.
10. Não apresente recomendações sem fundamento nos dados.

Seu objetivo é ajudar as pessoas a controlar
melhor seus custos mensais.
```

## Exemplos de interação

| Pergunta | Comportamento esperado |
|---|---|
| Quanto gastei este mês? | Soma das despesas registradas |
| Onde estou gastando mais? | Identificação da categoria principal |
| Quanto posso economizar? | Simulação de redução de despesas |
| Vou ultrapassar meu orçamento? | Comparação entre gastos e limites |
| Como posso reduzir meus custos? | Recomendações baseadas nos dados |

---

#  7. Aplicação Funcional

O projeto será desenvolvido utilizando Google Colab, Python e Gradio.

## Funcionalidades previstas

| Funcionalidade | Descrição |
|---|---|
| Registro de despesas | Cadastro de gastos |
| Análise mensal | Cálculo de receitas e despesas |
| Classificação inteligente | Organização por categorias |
| Previsão de custos | Estimativa de gastos futuros |
| Detector de excessos | Identificação de gastos elevados |
| Planejamento financeiro | Definição de limites mensais |
| Chat inteligente | Conversação com IA generativa |
| Histórico | Persistência do contexto |

## Organização do código

Os arquivos da aplicação estarão na pasta `src/`.

- `app.py`: interface do usuário.
- `agente.py`: comportamento e integração com IA.
- `analise.py`: análise de receitas e despesas.
- `simulador.py`: simulação e previsão de custos.
- `memoria.py`: persistência do contexto das conversas.

---

#  8. Avaliação e Métricas

A qualidade do agente será avaliada por meio de testes com dados simulados.

| Métrica | Objetivo |
|---|---|
| Assertividade | Verificar se as respostas estão corretas |
| Precisão dos cálculos | Comparar resultados com cálculos de referência |
| Segurança | Avaliar respostas sem informações inventadas |
| Personalização | Verificar recomendações conforme o perfil |
| Coerência | Avaliar a utilização do contexto anterior |

### Meta inicial

Alcançar 100% de acerto nos casos de teste matemáticos definidos, sem considerar essa meta como garantia de precisão em todas as respostas da IA.

---

#  9. Pitch do Projeto

O CustoCerto AI nasceu da necessidade de facilitar o controle financeiro mensal.

Muitas pessoas sabem quanto recebem, mas não conseguem identificar exatamente para onde vai seu dinheiro.

Pensando nisso, desenvolvi um agente financeiro inteligente que utiliza Python e Inteligência Artificial Generativa para analisar despesas, identificar padrões de consumo e antecipar possíveis excessos no orçamento.

O sistema permite registrar despesas, visualizar indicadores financeiros, realizar previsões e conversar com um assistente que apresenta recomendações personalizadas.

O diferencial está na combinação entre inteligência artificial e cálculos realizados diretamente em Python, proporcionando respostas mais transparentes e fundamentadas nos dados disponíveis.

Com o CustoCerto AI, o objetivo é transformar dados financeiros em informações úteis para decisões mais conscientes.

---

#  10. Estrutura do Repositório

O projeto mantém a organização de diretórios do repositório de referência da DIO, com adaptações para o contexto de controle e análise de custos mensais.

```text
📁 custocerto-ai/
│
├── 📄 README.md
│
├── 📁 data/
│   ├── historico_atendimento.csv
│   ├── perfil_financeiro.json
│   ├── orcamento_mensal.json
│   └── transacoes.csv
│
├── 📁 docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── 📁 src/
│   ├── app.py
│   ├── agente.py
│   ├── analise.py
│   ├── simulador.py
│   └── memoria.py
│
├── 📁 assets/
│   ├── dashboard.png
│   └── arquitetura.png
│
└── 📁 examples/
    └── README.md
```

---

#  11. Como Executar

O desenvolvimento será realizado no Google Colab.

1. Acesse o Google Colab.
2. Abra o notebook de desenvolvimento do projeto.
3. Instale as dependências necessárias.
4. Configure a chave da API de IA nos recursos seguros do ambiente.
5. Execute as células na ordem.
6. Carregue os dados financeiros de demonstração.
7. Utilize a interface para conversar com o agente.

## Dependências previstas

- pandas
- matplotlib
- gradio
- google-genai

As versões serão definidas no arquivo `requirements.txt`.

---

#  12. Autor e Créditos

**Projeto:** CustoCerto AI  
**Área:** Inteligência Artificial e Gestão Financeira  
**Linguagem:** Python  
**Ambiente:** Google Colab  
**Desafio:** Inteligência Artificial Generativa — DIO

Projeto desenvolvido como solução autoral para o desafio prático, utilizando conceitos de IA generativa, análise de dados, programação Python e experiência do usuário.

---

#  Aviso

O CustoCerto AI é um projeto demonstrativo de educação e organização financeira.

Suas previsões e recomendações não representam aconselhamento financeiro profissional nem ofertas de produtos financeiros.

Os dados utilizados para demonstração são fictícios.


