
# 📊 Base de Conhecimento — CustoCerto AI

## Dados Utilizados

O CustoCerto AI utiliza uma base de conhecimento composta por arquivos CSV e JSON com dados financeiros fictícios, criados para simular a realidade de um usuário que deseja controlar seus custos mensais.

Esses dados permitem que o agente analise receitas, despesas, categorias de consumo, limites de orçamento e objetivos financeiros, oferecendo respostas contextualizadas e recomendações personalizadas.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Recuperar conversas anteriores e manter o contexto das interações |
| `perfil_financeiro.json` | JSON | Personalizar análises e recomendações conforme os objetivos financeiros do usuário |
| `orcamento_mensal.json` | JSON | Comparar despesas realizadas com os limites planejados por categoria |
| `transacoes.csv` | CSV | Analisar receitas, despesas e padrões de consumo do usuário |

### Descrição dos dados

- **historico_atendimento.csv:** armazena perguntas e respostas anteriores para permitir continuidade nas conversas.
- **perfil_financeiro.json:** contém informações sobre renda, objetivos e preferências financeiras.
- **orcamento_mensal.json:** apresenta os limites de gastos definidos para cada categoria.
- **transacoes.csv:** registra movimentações financeiras, incluindo receitas e despesas.

> [!TIP]
> Os dados utilizados são fictícios e destinados exclusivamente à demonstração e aos testes do agente. A estrutura permite a inclusão futura de novos registros e categorias financeiras.

---

## Adaptações nos Dados

Os dados mockados foram adaptados para atender à proposta do CustoCerto AI, cujo foco principal é o controle, a análise e a previsão de custos mensais.

Foram realizadas as seguintes adaptações:

1. Substituição do perfil de investidor por um perfil financeiro voltado ao controle de despesas e objetivos de economia.
2. Adaptação do histórico de atendimento para registrar dúvidas relacionadas a receitas, despesas, orçamento e oportunidades de economia.
3. Utilização de transações financeiras classificadas por categorias, como moradia, alimentação, transporte, saúde e lazer.
4. Criação do arquivo `orcamento_mensal.json` para armazenar limites de gastos por categoria.
5. Inclusão de informações sobre metas financeiras para personalizar as recomendações do agente.

### Exemplo de perfil financeiro

```json
{
  "nome": "Cliente Demonstrativo",
  "renda_mensal": 4500.00,
  "objetivo_financeiro": "Economizar dinheiro",
  "meta_economia_mensal": 500.00,
  "perfil": "Conservador",
  "preferencia": "Reduzir despesas variaveis"
}
```

### Exemplo de orçamento mensal

```json
{
  "mes": "2026-11",
  "limites": {
    "Moradia": 1500.00,
    "Alimentacao": 700.00,
    "Transporte": 350.00,
    "Saude": 250.00,
    "Lazer": 200.00,
    "Outros": 300.00
  }
}
```

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos CSV e JSON são armazenados na pasta `data/` do projeto e carregados por meio de funções desenvolvidas em Python.

A biblioteca Pandas será utilizada para leitura e manipulação dos arquivos CSV, enquanto a biblioteca JSON será utilizada para carregar os dados estruturados do perfil financeiro e do orçamento mensal.

O processo de carregamento será realizado no início da aplicação, permitindo que o agente consulte as informações sempre que necessário.

Os dados também poderão ser atualizados durante a utilização do sistema, conforme novos registros financeiros forem adicionados.

### Como os dados são usados no prompt?

Os dados não serão inseridos integralmente no System Prompt.

O System Prompt será responsável por definir a identidade, o comportamento e as regras de segurança do CustoCerto AI.

As informações financeiras serão consultadas dinamicamente conforme a necessidade de cada pergunta.

O funcionamento seguirá estas etapas:

1. O usuário envia uma pergunta ao agente.
2. A IA interpreta a intenção da pergunta.
3. O sistema identifica quais informações financeiras são necessárias.
4. Python consulta os arquivos da base de conhecimento.
5. As funções de análise realizam os cálculos necessários.
6. Os resultados são organizados e enviados à IA como contexto.
7. A IA gera uma resposta utilizando os dados disponíveis.
8. O agente apresenta a resposta ao usuário.

Essa estratégia reduz o envio desnecessário de informações e contribui para respostas mais precisas e contextualizadas.

### Exemplo de utilização

Se o usuário perguntar:

"Qual categoria está consumindo mais dinheiro do meu orçamento?"

O agente consultará o arquivo `transacoes.csv`, agrupará as despesas por categoria e identificará aquela com maior valor.

Em seguida, comparará o resultado com os limites registrados em `orcamento_mensal.json` e apresentará uma análise.

---

## Exemplo de Contexto Montado

Abaixo está um exemplo ilustrativo de como as informações financeiras são organizadas antes de serem encaminhadas ao modelo de IA.

```text
Você é o CustoCerto AI, um agente especializado
em gestão de custos mensais.

Dados do Cliente:

- Nome: Cliente Demonstrativo
- Renda mensal: R$ 4.500,00
- Objetivo: Economizar dinheiro
- Meta de economia: R$ 500,00
- Perfil financeiro: Conservador

Resumo Financeiro:

- Total de receitas: R$ 4.500,00
- Total de despesas: R$ 3.455,00
- Saldo disponível: R$ 1.045,00

Despesas por Categoria:

- Moradia: R$ 1.380,00
- Alimentação: R$ 770,00
- Transporte: R$ 250,00
- Lazer: R$ 55,00

Orçamento Planejado:

- Moradia: R$ 1.500,00
- Alimentação: R$ 700,00
- Transporte: R$ 350,00
- Lazer: R$ 200,00

Objetivo da Análise:

Identificar categorias que ultrapassaram
os limites planejados e sugerir oportunidades
de economia.

Regras:

- Não inventar informações financeiras.
- Utilizar somente os dados disponíveis.
- Diferenciar valores registrados de previsões.
- Informar quando faltarem informações.
- Basear recomendações nos resultados calculados.
```

---

## Segurança e Confiabilidade dos Dados

Para garantir a qualidade das informações utilizadas pelo agente, serão adotadas as seguintes práticas:

- Utilização de dados fictícios durante o desenvolvimento.
- Validação dos valores e formatos dos arquivos.
- Identificação de registros incompletos ou inconsistentes.
- Execução dos cálculos financeiros por funções Python.
- Proibição de inventar transações ou valores.
- Proteção de credenciais e informações sensíveis.
- Utilização de informações financeiras somente conforme a finalidade do sistema.

Caso não existam dados suficientes para responder a uma pergunta, o agente deverá informar essa limitação ao usuário.

---

## Resultado Esperado

A integração da base de conhecimento permitirá que o CustoCerto AI transforme dados financeiros em informações úteis para o usuário.

Com essa estrutura, o agente poderá analisar despesas, acompanhar limites de orçamento, identificar padrões de consumo, antecipar possíveis excessos e sugerir oportunidades de economia.

O objetivo é oferecer uma experiência financeira mais inteligente, consultiva e personalizada, utilizando IA Generativa integrada a cálculos e análises realizados em Python.

---

**Projeto:** CustoCerto AI  
**Desafio:** Inteligência Artificial Generativa — DIO  
**Tecnologias:** Python, Pandas, JSON e IA Generativa  
**Ambiente de desenvolvimento:** Google Colab
