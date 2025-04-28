# Sprint 8: Análise de Marketing e Métricas de Negócio (Y.Afisha)

## Qual o objetivo do sprint?

Neste sprint, meu papel foi analisar a performance das campanhas de marketing do serviço Y.Afisha. O objetivo principal era entender como os usuários interagem com o serviço, desde a primeira visita até a compra, e avaliar a eficácia dos diferentes canais de marketing. Para isso, precisei:

1.  **Preparar os Dados:** Carreguei e processei três conjuntos de dados: custos de marketing (`costs_us.csv`), logs de pedidos (`orders_log_us.csv`) e logs de visitas ao site (`visits_log_us.csv`). Isso envolveu renomear colunas para padronização, corrigir tipos de dados (especialmente datas e horas) e verificar valores ausentes ou duplicados.
2.  **Analisar Métricas de Produto:** Calculei e visualizei métricas chave de engajamento do usuário, como:
    *   Usuários ativos diários, semanais e mensais (DAU, WAU, MAU).
    *   Número de sessões por dia.
    *   Duração média das sessões.
    *   Taxa de retenção dos usuários (usando análise de coorte baseada no mês do primeiro acesso).
3.  **Analisar Métricas de Vendas:** Investiguei o comportamento de compra, calculando:
    *   Tempo médio desde a primeira visita até a primeira compra (conversão).
    *   Número médio de pedidos por cliente em diferentes períodos (dia, semana, mês).
    *   Volume médio e mediano de compra (receita por pedido).
    *   Valor vitalício do cliente (LTV), analisado também por coorte.
4.  **Analisar Métricas de Marketing:** Avaliei a performance dos investimentos em marketing, focando em:
    *   Custo total de marketing, custo por origem de anúncio e distribuição dos custos ao longo do tempo.
    *   Custo de aquisição de cliente (CAC) por origem de anúncio e por coorte.
    *   Retorno sobre o investimento em marketing (ROI/ROMI) geral, por origem e por coorte.
5.  **Tirar Conclusões e Recomendar Ações:** Com base em todas as métricas analisadas, formulei conclusões sobre a rentabilidade dos canais de marketing e forneci recomendações para otimizar a estratégia de marketing futura.

## Quais tecnologias usei?

Para realizar esta análise de marketing detalhada, utilizei as seguintes ferramentas e bibliotecas Python:

*   **Python:** Linguagem base para todo o processamento e análise.
*   **Pandas:** Essencial para carregar os dados (`pd.read_csv`), limpar (`.rename()`, `pd.to_datetime()`, `.astype()`, `.isnull()`), agregar (`.groupby()`, `.agg()`, `.nunique()`, `.size()`, `.mean()`, `.median()`, `.sum()`), transformar (`.dt.date`, `.dt.to_period()`, `.dt.isocalendar()`, `.transform()`, `.apply()`, `.resample()`), mesclar (`pd.merge`) e criar tabelas dinâmicas (`.pivot_table()`).
*   **NumPy:** Usado para operações numéricas, possivelmente de forma implícita ou para cálculos específicos se necessário.
*   **Matplotlib (`pyplot`) / Seaborn:** Para criar visualizações gráficas, incluindo gráficos de linha (DAU/WAU/MAU, sessões), histogramas (distribuição do tempo de conversão), heatmaps (retenção de coorte, LTV por coorte) e gráficos de barras (custos, CAC, ROI por origem).

## Quais competências eu consegui?

Ao concluir este sprint, demonstrei e aprimorei as seguintes competências:

*   **Análise de Métricas de Produto e Marketing:** Calculei, interpretei e visualizei uma ampla gama de métricas essenciais para negócios online (DAU/WAU/MAU, LTV, CAC, ROI/ROMI, retenção, conversão).
*   **Análise de Coorte:** Apliquei análise de coorte para entender o comportamento do usuário e a rentabilidade ao longo do tempo, um método poderoso para avaliar a eficácia do marketing e o valor do cliente.
*   **Pré-processamento de Dados:** Realizei a limpeza e organização de dados provenientes de múltiplas fontes, garantindo consistência e adequação dos tipos de dados para análise.
*   **Agregação e Manipulação Avançada de Dados:** Utilizei `groupby`, `resample`, `pivot_table` e `merge` para agregar e combinar dados em diferentes níveis (diário, semanal, mensal, por usuário, por origem, por coorte).
*   **Análise Financeira de Marketing:** Calculei e interpretei métricas financeiras cruciais como CAC, LTV e ROI/ROMI para avaliar a rentabilidade das campanhas de marketing.
*   **Visualização de Dados Complexos:** Criei visualizações adequadas (incluindo heatmaps de coorte) para comunicar padrões e resultados de forma clara e impactante.
*   **Pensamento Estratégico e Geração de Recomendações:** Traduzi as descobertas da análise de dados em recomendações de negócios concretas e acionáveis para a otimização da estratégia de marketing.

Este sprint proporcionou uma experiência prática valiosa na análise ponta a ponta de dados de marketing, combinando métricas de produto, vendas e custos para avaliar o desempenho e orientar decisões estratégicas.