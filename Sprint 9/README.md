# Sprint 9: Análise de Teste A/B e Priorização de Hipóteses

## Qual o objetivo do sprint?

Neste sprint, o foco foi analisar um teste A/B realizado por uma loja online e também priorizar hipóteses para melhorar o desempenho. As principais tarefas foram:

1.  **Priorização de Hipóteses:**
    *   Carreguei um arquivo com hipóteses, seus níveis de impacto, confiança, esforço e alcance (`hypotheses_us.csv`).
    *   Calculei as pontuações **ICE (Impact, Confidence, Effort)** e **RICE (Reach, Impact, Confidence, Effort)** para cada hipótese.
    *   Comparei os rankings gerados pelos dois métodos, entendendo como o fator 'Alcance' (Reach) no RICE altera a prioridade, e justifiquei a escolha do método mais adequado para o contexto (RICE, devido à natureza online da loja).
2.  **Análise do Teste A/B:**
    *   Carreguei e preparei os dados de pedidos (`orders_us.csv`) e visitas (`visits_us.csv`), corrigindo tipos de dados (datas), renomeando colunas e, crucialmente, identificando e removendo usuários que estavam presentes em ambos os grupos de teste (A e B), o que invalidaria a análise.
    *   **Análise Exploratória e Visual:**
        *   Calculei e plotei métricas cumulativas ao longo do tempo para ambos os grupos (A e B), como receita acumulada, tamanho médio acumulado do pedido e taxa de conversão acumulada.
        *   Plotei a diferença relativa entre as métricas acumuladas dos grupos para visualizar a dinâmica da performance do teste.
    *   **Identificação e Tratamento de Outliers:**
        *   Analisei a distribuição do número de pedidos por usuário e da receita por pedido.
        *   Utilizei percentis (95º e 99º) e gráficos de dispersão para identificar valores anômalos.
        *   Defini limiares para filtrar esses outliers e criei um conjunto de dados "limpo".
    *   **Teste de Significância Estatística:**
        *   Utilizei o teste não paramétrico **Mann-Whitney U** para comparar as distribuições entre os grupos A e B para métricas chave (taxa de conversão e tamanho médio do pedido/número de pedidos por usuário). *Nota: A análise foi feita comparando as séries de dados brutos e também as séries após a filtragem dos outliers.*
        *   Formulei as hipóteses nula (H₀ - não há diferença) e alternativa (H₁ - há diferença).
        *   Defini um nível de significância (alfa = 0.05).
        *   Interpretei os p-valores para decidir se rejeitava ou não a hipótese nula, tanto para os dados brutos quanto para os filtrados.
    *   **Conclusão do Teste:** Com base na análise gráfica (estabilidade das métricas cumulativas) e nos resultados dos testes estatísticos (especialmente nos dados filtrados), tomei uma decisão sobre o resultado do teste A/B (declarar um vencedor, parar ou continuar o teste) e justifiquei a escolha.

## Quais tecnologias usei?

As seguintes ferramentas e bibliotecas Python foram utilizadas:

*   **Python:** Linguagem principal para a análise.
*   **Pandas:** Para carregar os dados (`pd.read_csv`), limpar (`.info()`, `.astype()`, `.drop_duplicates()`, tratamento de usuários duplicados entre grupos), agregar (`.groupby()`, `.agg()`), calcular métricas cumulativas (`.cumsum()`) e manipular os DataFrames.
*   **NumPy:** Para operações numéricas, como cálculo de percentis (`np.percentile`).
*   **Matplotlib (`pyplot`) / Seaborn:** Para criar visualizações como gráficos de linha (métricas cumulativas, diferença relativa), gráficos de dispersão (outliers de receita) e histogramas (se aplicável, embora não explicitamente mostrado para pedidos/receita na versão final, foi usado para entender a distribuição).
*   **SciPy (`scipy.stats`):** Essencial para realizar o teste de Mann-Whitney U (`st.mannwhitneyu`) para comparar as amostras dos grupos A и B.

## Quais competências eu consegui?

Ao completar este sprint, demonstrei e aprimorei competências em:

*   **Priorização de Hipóteses:** Apliquei e comparei os frameworks ICE e RICE, compreendendo a importância do fator "Alcance" na priorização.
*   **Planejamento e Análise de Teste A/B:** Executei o fluxo completo de análise de um teste A/B, desde a limpeza específica (remoção de usuários duplicados entre grupos) até a análise estatística e tomada de decisão.
*   **Análise de Métricas Cumulativas:** Calculei, visualizei e interpretei gráficos de métricas cumulativas para entender a dinâmica e a estabilidade de um teste ao longo do tempo.
*   **Detecção e Tratamento de Outliers:** Utilizei métodos estatísticos (percentis) e visuais (scatter plots) para identificar dados anômalos e avaliei o impacto da remoção deles nos resultados estatísticos.
*   **Aplicação de Testes Estatísticos Não Paramétricos:** Selecionei e apliquei corretamente o teste Mann-Whitney U para comparar duas amostras independentes quando a normalidade não podia ser assumida (comum em métricas como receita ou conversão).
*   **Interpretação Estatística:** Interpretei p-valores e tomei decisões estatísticas baseadas no nível de significância alfa, comparando resultados com dados brutos e filtrados.
*   **Tomada de Decisão Baseada em Dados:** Formulei uma conclusão clara sobre o teste A/B, recomendando ações (parar o teste, declarar vencedor) com base nas evidências gráficas e estatísticas.

Este sprint foi crucial para consolidar o conhecimento sobre priorização de ideias e a metodologia completa de análise de testes A/B, incluindo a importância da limpeza de dados e da robustez estatística.