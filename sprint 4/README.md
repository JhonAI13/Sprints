# Sprint 4: Análise de Planos de Telecomunicações (Megaline)

## Qual o objetivo do sprint?

Neste sprint, atuei como analista para a Megaline, uma empresa de telecomunicações. O objetivo era analisar o comportamento dos clientes em dois planos pré-pagos, Surf e Ultimate, para determinar qual deles gera mais receita. Essa análise ajudaria o departamento comercial a ajustar o orçamento de publicidade de forma mais eficaz. As principais tarefas foram:

1.  **Carregar e Pré-processar Dados:** Ler os dados de 500 clientes distribuídos em várias tabelas (chamadas, mensagens, internet, usuários, planos). Realizei a limpeza necessária, corrigindo tipos de dados (especialmente datas), tratando valores ausentes e verificando duplicatas.
2.  **Agregar Dados por Usuário e Mês:** Calculei o consumo mensal de cada usuário para chamadas (número e duração em minutos), mensagens (quantidade) e dados de internet (volume em MB/GB). Os minutos e GBs foram arredondados para cima, conforme as regras de cobrança.
3.  **Calcular Receita Mensal:** Criei uma lógica para calcular a receita mensal gerada por cada usuário, considerando a taxa base do plano e as cobranças adicionais por exceder os limites de minutos, mensagens ou dados incluídos no pacote.
4.  **Analisar o Comportamento do Usuário:** Comparei o consumo médio mensal (minutos, mensagens, dados) e a receita média gerada pelos usuários dos planos Surf e Ultimate. Usei estatísticas descritivas e visualizações (histogramas, boxplots) para identificar padrões e diferenças.
5.  **Testar Hipóteses Estatísticas:** Formulei e testei hipóteses para verificar se:
    *   A receita média dos usuários do plano Ultimate difere significativamente da receita média dos usuários do plano Surf.
    *   A receita média dos usuários da área metropolitana NY-NJ difere da receita dos usuários de outras regiões.

## Quais tecnologias usei?

As seguintes ferramentas e bibliotecas Python foram empregadas neste sprint:

*   **Python:** Linguagem base para todo o processo.
*   **Pandas:** Crucial para carregar os dados (`pd.read_csv`), limpar (`.info()`, `.astype()`, tratamento de NaNs), agregar (`.groupby()`), mesclar tabelas (`pd.merge`) e realizar cálculos sobre os DataFrames.
*   **NumPy:** Utilizado para operações numéricas, como o arredondamento para cima (`np.ceil`) dos minutos e gigabytes para o cálculo correto da receita.
*   **Matplotlib (`pyplot`) / Seaborn:** Para criar visualizações como histogramas, gráficos de barras e boxplots, facilitando a análise comparativa do comportamento dos usuários e da receita entre os planos.
*   **SciPy (`scipy.stats`):** Para realizar os testes t de Student (`st.ttest_ind`), que foram usados para testar as hipóteses sobre as diferenças nas médias de receita.
*   **Calendar (`month_name`):** Para mapear números de mês para nomes, melhorando a legibilidade dos agrupamentos e gráficos mensais.

## Quais competências eu consegui?

Ao completar este sprint, desenvolvi e demonstrei as seguintes competências:

*   **Pré-processamento de Dados Complexos:** Trabalhei com múltiplos arquivos, corrigi tipos de dados (especialmente datas e numéricos), e tratei valores ausentes de forma contextualizada.
*   **Agregação e Transformação de Dados:** Agrupei dados em diferentes níveis (usuário, mês) e calculei métricas complexas como a receita mensal, aplicando regras de negócio específicas dos planos.
*   **Engenharia de Atributos:** Criei colunas derivadas importantes (mês, nome do mês, receita mensal) para facilitar a análise.
*   **Análise Comparativa de Grupos:** Usei estatísticas descritivas (média, variância, desvio padrão) e visualizações (histogramas, boxplots) para comparar efetivamente o comportamento de usuários em diferentes planos (Surf vs. Ultimate).
*   **Teste de Hipóteses Estatísticas:** Formulei hipóteses nula e alternativa, selecionei o teste estatístico apropriado (teste t), defini um nível de significância (alfa), executei o teste e interpretei os resultados (p-valor) para tirar conclusões estatisticamente fundamentadas sobre as diferenças de receita.
*   **Visualização de Dados para Comparação:** Criei gráficos comparativos claros para ilustrar as diferenças e semelhanças no uso e na receita entre os planos ao longo do tempo.
*   **Tradução de Requisitos de Negócio em Análise:** Transformei a pergunta de negócio (qual plano gera mais receita?) em um plano de análise de dados estruturado, culminando em uma recomendação baseada em evidências.

Este sprint foi um exercício prático completo, desde a limpeza de dados até a aplicação de estatística inferencial para responder a uma pergunta de negócio relevante.