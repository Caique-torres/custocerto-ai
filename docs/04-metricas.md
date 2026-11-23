
#  Avaliação e Métricas — CustoCerto AI

## Como Avaliar seu Agente

A avaliação do CustoCerto AI será realizada por meio de duas abordagens complementares:

1. **Testes estruturados:** perguntas financeiras com respostas esperadas, utilizando os dados disponíveis na base de conhecimento.
2. **Feedback dos usuários:** pessoas testam o agente e avaliam a qualidade das respostas, facilidade de utilização e clareza das recomendações.

O objetivo é verificar se o agente consegue interpretar perguntas, consultar corretamente os dados financeiros, realizar cálculos e apresentar recomendações coerentes.

Os testes serão realizados utilizando dados financeiros fictícios armazenados na pasta `data/`.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | Se o agente responde corretamente às perguntas financeiras | Consultar o total de despesas e comparar com o resultado calculado em Python |
| **Precisão dos cálculos** | Se os valores apresentados correspondem aos registros financeiros | Somar as despesas de alimentação no `transacoes.csv` |
| **Segurança** | Se o agente evita inventar informações financeiras | Perguntar sobre uma transação inexistente |
| **Coerência** | Se as recomendações fazem sentido para o perfil financeiro | Sugerir redução de despesas considerando a renda e os objetivos do usuário |
| **Contextualização** | Se o agente utiliza informações de conversas anteriores | Perguntar novamente sobre uma meta de economia já informada |
| **Previsão** | Se as estimativas são calculadas corretamente com base nos dados disponíveis | Estimar os gastos até o final do mês |
| **Experiência do usuário** | Se as respostas são claras e fáceis de compreender | Solicitar uma análise do orçamento mensal |

> [!TIP]
> Convide de 3 a 5 pessoas para testar o CustoCerto AI. Cada participante poderá avaliar as respostas com notas de 1 a 5, considerando clareza, precisão, utilidade e facilidade de utilização. Explique que os dados utilizados representam um cliente fictício.

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de despesas

- **Pergunta:** "Quanto gastei com alimentação neste mês?"
- **Resposta esperada:** O agente consulta o arquivo `transacoes.csv`, soma as despesas da categoria Alimentação e apresenta o resultado correto.
- **Validação:** Comparar a resposta com o cálculo realizado em Python.
- **Resultado:** [ ] Correto [ ] Incorreto

### Teste 2: Identificação de gastos excessivos

- **Pergunta:** "Estou gastando mais do que deveria com alimentação?"
- **Resposta esperada:** O agente compara as despesas registradas com o limite definido no arquivo `orcamento_mensal.json` e informa se o orçamento foi ultrapassado.
- **Validação:** Conferir se a comparação e o valor excedente estão corretos.
- **Resultado:** [ ] Correto [ ] Incorreto

### Teste 3: Planejamento de economia

- **Pergunta:** "Como posso economizar R$ 500,00 por mês?"
- **Resposta esperada:** O agente analisa as despesas disponíveis e apresenta sugestões de redução compatíveis com o orçamento e os objetivos financeiros do usuário.
- **Validação:** Verificar se as recomendações possuem fundamento nos dados registrados.
- **Resultado:** [ ] Correto [ ] Incorreto

### Teste 4: Pergunta fora do escopo

- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** O agente informa que sua especialidade é o controle e a análise de custos mensais.
- **Validação:** Verificar se o agente evita fornecer informações sem relação com sua finalidade.
- **Resultado:** [ ] Correto [ ] Incorreto

### Teste 5: Informação inexistente

- **Pergunta:** "Quanto gastei em uma compra que não está registrada?"
- **Resposta esperada:** O agente informa que não encontrou essa transação na base de conhecimento e solicita o registro da despesa.
- **Validação:** Verificar se o agente evita inventar valores.
- **Resultado:** [ ] Correto [ ] Incorreto

### Teste 6: Previsão de custos

- **Pergunta:** "Quanto devo gastar até o final deste mês?"
- **Resposta esperada:** O agente utiliza as despesas registradas e o período transcorrido para calcular uma estimativa de gastos futuros.
- **Validação:** Conferir o cálculo e verificar se o resultado foi apresentado como previsão, não como valor garantido.
- **Resultado:** [ ] Correto [ ] Incorreto

### Teste 7: Continuidade da conversa

- **Pergunta inicial:** "Minha meta é economizar R$ 500,00 por mês."
- **Pergunta seguinte:** "Quanto falta para atingir minha meta?"
- **Resposta esperada:** O agente recupera o contexto anterior e calcula quanto ainda falta economizar, considerando os valores registrados.
- **Validação:** Verificar se o contexto da conversa foi preservado corretamente.
- **Resultado:** [ ] Correto [ ] Incorreto

---

## Resultados

Após a execução dos testes, serão registrados os resultados e as oportunidades de melhoria identificadas.

### O que funcionou bem:

- Consulta e análise das despesas registradas.
- Identificação das categorias com maiores gastos.
- Comparação entre despesas e limites do orçamento.
- Realização de cálculos financeiros utilizando Python.
- Respostas contextualizadas com base nos dados disponíveis.
- Recomendações voltadas à organização financeira.

### O que pode melhorar:

- Aprimorar a precisão das previsões de custos.
- Melhorar a interpretação de perguntas com linguagem natural.
- Ampliar a quantidade de categorias financeiras.
- Melhorar a persistência do histórico de conversas.
- Desenvolver um dashboard para visualização dos resultados.
- Ampliar os testes com diferentes perfis financeiros.

**Observação:** os itens acima representam objetivos e pontos de avaliação do projeto. Os resultados definitivos deverão ser atualizados após a execução dos testes.

---

## Métricas Avançadas (Opcional)

Além das métricas de qualidade, o CustoCerto AI poderá utilizar indicadores técnicos para acompanhar o desempenho da aplicação.

| Métrica | Descrição |
|---------|-----------|
| Latência | Tempo necessário para gerar uma resposta |
| Consumo de tokens | Quantidade de tokens utilizados pela IA |
| Custo da API | Acompanhamento dos custos de utilização do modelo |
| Taxa de erros | Percentual de falhas durante as interações |
| Precisão dos cálculos | Comparação entre resultados do agente e valores de referência |
| Taxa de respostas válidas | Percentual de respostas que seguem as regras definidas |

### Ferramentas de monitoramento

- **Python:** execução de testes automatizados e validação dos cálculos.
- **Pandas:** análise dos resultados dos testes.
- **Logs:** registro de erros e tempo de execução.
- **LangFuse:** possibilidade de monitoramento das interações com modelos de IA.
- **LangWatch:** possibilidade de avaliação e observabilidade do agente.

---

## Indicadores de Desempenho

Como metas iniciais de qualidade, serão considerados os seguintes indicadores:

| Indicador | Meta inicial |
|-----------|--------------|
| Precisão dos cálculos financeiros | 100% nos casos de teste definidos |
| Respostas baseadas nos dados | 100% nos testes de consulta financeira |
| Tratamento de perguntas fora do escopo | 100% nos casos de teste |
| Continuidade do contexto | 90% ou mais nos testes realizados |
| Avaliação dos usuários | Média mínima de 4 em 5 |

As metas são referências para avaliação e não representam resultados já alcançados.

---

## Conclusão

A avaliação do CustoCerto AI permitirá verificar a qualidade das respostas, a precisão dos cálculos e a capacidade de interpretar informações financeiras.

A combinação de testes estruturados, validação com Python e feedback dos usuários contribuirá para melhorar continuamente o agente.

O objetivo é desenvolver uma solução confiável, acessível e inteligente, capaz de transformar dados financeiros em informações úteis para o controle de custos mensais e a identificação de oportunidades de economia.

---

**Projeto:** CustoCerto AI  
**Desafio:** Agente Financeiro Inteligente com IA Generativa — DIO  
**Linguagem:** Python  
**IA Generativa:** Gemini API  
**Ambiente de desenvolvimento:** Google Colab
