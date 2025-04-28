# Sprint 7: Análise de Dados de Corridas de Táxi em Chicago

## Qual o objetivo do sprint?

Neste sprint, meu trabalho foi analisar dados sobre corridas de táxi na cidade de Chicago. O objetivo era entender melhor a dinâmica desse mercado, focando em três aspectos principais:

1.  **Empresas de Táxi:** Identificar quais empresas realizam mais corridas e analisar a concentração do mercado.
2.  **Bairros de Destino:** Descobrir quais bairros são os destinos mais populares para as corridas de táxi.
3.  **Impacto do Clima:** Investigar especificamente as corridas do Loop para o Aeroporto O'Hare e testar se as condições climáticas (bom tempo vs. mau tempo) afetam significativamente a duração média dessas viagens.

Para alcançar isso, precisei primeiro **explorar e preparar os dados** das tabelas fornecidas (`taxi_company_trips`, `neighborhood_trip_avg`, `loop_to_ohare_trips`), verificando tipos de dados (corrigindo a coluna de data `start_ts`) e entendendo a estrutura. Depois, realizei a **análise exploratória (EDA)** com visualizações para entender as distribuições e, por fim, executei um **teste de hipótese estatística** para responder à questão sobre o clima.

## Quais tecnologias usei?

As principais ferramentas e bibliotecas Python utilizadas neste sprint foram:

*   **Python:** Como linguagem base.
*   **Pandas:** Para carregar os dados (`pd.read_csv`), inspecionar (`.info()`, `.describe()`, `.sample()`), limpar (corrigir tipo de data com `pd.to_datetime`), e manipular os dados (filtrar, ordenar com `.sort_values()`).
*   **NumPy:** Usado para operações numéricas, possivelmente de forma implícita pelo Pandas ou SciPy.
*   **Matplotlib (`pyplot`) / Seaborn:** Para criar os gráficos de barras (`sns.barplot`) que visualizaram o número de corridas por empresa e por bairro.
*   **SciPy (`scipy.stats`):** Para realizar o teste t de Student (`st.ttest_ind`) na comparação das durações médias das corridas sob diferentes condições climáticas.

## Quais competências eu consegui?

Ao completar este sprint, demonstrei e reforcei as seguintes competências:

*   **Análise Exploratória de Dados (EDA):** Utilizei métodos descritivos e visuais para entender as características dos dados, identificar padrões (como concentração de mercado em empresas e bairros) e anomalias (tipos de dados incorretos).
*   **Limpeza e Preparação de Dados:** Identifiquei e corrigi problemas de tipo de dados (conversão de strings para datetime).
*   **Visualização de Dados:** Criei e interpretei gráficos de barras para comparar quantidades e identificar líderes de mercado (empresas e bairros).
*   **Teste de Hipóteses Estatísticas:**
    *   Formulei claramente as hipóteses nula (H₀) e alternativa (H₁) para a questão sobre o impacto do clima.
    *   Selecionei e apliquei corretamente um teste t para amostras independentes.
    *   Interpretei o p-valor resultante em relação ao nível de significância (alfa) para tirar uma conclusão estatística.
    *   Entendi a importância de parâmetros como `equal_var=False` quando as variâncias dos grupos podem ser diferentes.
*   **Manipulação de Dados com Pandas:** Filtrei dados com base em condições (clima bom vs. ruim), calculei médias e ordenei dados para análise.
*   **Pensamento Crítico e Conclusão:** Integrei os resultados da EDA e do teste de hipóteses para formar uma conclusão geral sobre os padrões das corridas de táxi e o efeito do clima em uma rota específica.

Este sprint me permitiu aplicar tanto a análise exploratória quanto a estatística inferencial para investigar padrões e testar uma hipótese específica em dados de transporte urbano.