# Sprint 6: Análise de Vendas de Videogames

## Qual o objetivo do sprint?

Neste sprint, o objetivo foi realizar uma análise profunda em um conjunto de dados históricos sobre vendas de videogames. A meta era identificar padrões que pudessem explicar o sucesso de um jogo e ajudar a planejar campanhas futuras (como para 2017). As principais etapas incluíram:

1.  **Preparação dos Dados:** Carregar o arquivo `games.csv`, padronizar nomes de colunas, verificar e corrigir tipos de dados (ano, pontuações), lidar com valores ausentes (incluindo o valor 'tbd' em `user_score`) e calcular as vendas totais por jogo.
2.  **Análise Exploratória de Dados (EDA):**
    *   Analisar a quantidade de jogos lançados por ano para identificar períodos de crescimento e declínio na indústria.
    *   Investigar as vendas por plataforma ao longo do tempo, identificando plataformas líderes históricas, seus ciclos de vida (surgimento, pico, desaparecimento) e determinando um período de dados relevante para a análise focada em 2017 (sugestão: 2013-2016).
    *   Comparar as vendas globais de jogos entre as plataformas mais relevantes usando boxplots para entender a dispersão e as vendas médias.
    *   Verificar a correlação entre as avaliações (da crítica e dos usuários) e as vendas totais, tanto para uma plataforma específica (ex: PS4) quanto em geral para as plataformas relevantes.
    *   Analisar a distribuição de vendas por gênero, identificando os mais e menos lucrativos.
3.  **Criação de Perfis Regionais:** Analisar as preferências de mercado para as principais regiões (América do Norte - NA, Europa - EU, Japão - JP), identificando:
    *   As 5 principais plataformas em vendas.
    *   Os 5 principais gêneros em vendas.
    *   O impacto da classificação ESRB nas vendas de cada região.
4.  **Teste de Hipóteses Estatísticas:** Testar formalmente se:
    *   As classificações médias de usuários das plataformas Xbox One e PC são diferentes.
    *   As classificações médias de usuários dos gêneros Action e Sports são diferentes.

## Quais tecnologias usei?

Para essa análise, utilizei um conjunto de ferramentas padrão em Data Science com Python:

*   **Python:** Linguagem de programação principal.
*   **Pandas:** Para carregamento (`pd.read_csv`), manipulação, limpeza (`.fillna()`, `.astype()`, `.duplicated()`, `.drop_duplicates()`), agregação (`.groupby()`, `.value_counts()`) e transformação dos dados.
*   **NumPy:** Para operações numéricas, incluindo o cálculo de correlação (`np.corrcoef`).
*   **Matplotlib (`pyplot`):** Para a criação de gráficos base, como histogramas e gráficos de barras.
*   **Seaborn:** Para visualizações estatísticas mais elaboradas, como boxplots e scatter plots, complementando o Matplotlib.
*   **SciPy (`scipy.stats`):** Para realizar os testes de hipóteses estatísticas (teste t de Student - `st.ttest_ind`).

## Quais competências eu consegui?

Com a conclusão deste sprint, demonstrei e reforcei competências em:

*   **Limpeza e Pré-processamento de Dados:** Tratei eficientemente valores ausentes (NaN, 'tbd'), corrigi tipos de dados e padronizei a estrutura do DataFrame.
*   **Análise Exploratória de Dados (EDA):** Utilizei estatísticas descritivas e visualizações para identificar tendências temporais (lançamentos, ciclos de vida), comparar distribuições (vendas por plataforma/gênero) e investigar relações (scores vs. vendas).
*   **Análise Temporal e Identificação de Períodos Relevantes:** Analisei dados históricos para entender a dinâmica do mercado e justificar a escolha de um período específico para análise preditiva.
*   **Análise de Correlação:** Avaliei a força da relação linear entre variáveis numéricas (pontuações e vendas).
*   **Segmentação e Análise Regional:** Criei perfis de usuário distintos para diferentes mercados geográficos, identificando preferências locais por plataformas, gêneros e classificações etárias.
*   **Teste de Hipóteses Estatísticas:** Formulei hipóteses nula e alternativa, apliquei o teste t de Student corretamente (considerando a variância das amostras), interpretei p-valores e tomei decisões baseadas em significância estatística.
*   **Visualização de Dados:** Selecionei e configurei diferentes tipos de gráficos (barras, linhas, boxplots, scatter plots) para comunicar eficazmente os resultados da análise.
*   **Pensamento Crítico e Conclusão Baseada em Dados:** Sintetizei as descobertas das diversas análises para tirar conclusões gerais sobre o mercado de videogames e as diferenças regionais.

Este sprint foi uma prática valiosa na aplicação de um conjunto diversificado de técnicas de análise para extrair insights significativos de dados históricos e testar hipóteses de negócio.