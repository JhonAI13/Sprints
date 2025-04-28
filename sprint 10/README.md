# Sprint 10: Análise de Dados de Restaurantes nos EUA

## Qual o objetivo do sprint?

Neste sprint, o objetivo foi mergulhar em um conjunto de dados sobre restaurantes nos Estados Unidos (`rest_data_us_upd.csv`) para realizar uma análise exploratória detalhada. As principais metas foram:

1.  **Carregar e Preparar os Dados:** Ler o arquivo CSV, inspecionar as colunas (`.info()`, `.head()`), corrigir os tipos de dados para otimizar o uso de memória (`.astype()` para int8, boolean, category, int16) e garantir que estavam adequados para análise. Tratei valores ausentes na coluna `chain` (preenchendo com `False`) e identifiquei e removi uma linha duplicada específica. Além disso, fiz uma pequena engenharia de atributos extraindo o nome da rua (`rua`) da coluna `address`.
2.  **Análise Exploratória de Dados (EDA):**
    *   Investigar a distribuição dos **tipos de estabelecimentos** (Restaurant, Cafe, etc.) e a proporção entre estabelecimentos de **rede (chain)** e independentes.
    *   Analisar como os tipos de estabelecimento se distribuem entre as redes e os independentes.
    *   Comparar o **número de assentos (`number`)** entre estabelecimentos de rede e não rede, utilizando estatísticas descritivas (`.describe()`) e visualizações.
    *   Calcular e visualizar a **média de assentos por tipo de estabelecimento**.
    *   Analisar a **distribuição geográfica** dos restaurantes por rua, identificando as ruas com maior concentração e quantas ruas possuem apenas um estabelecimento.
    *   Explorar a **relação entre o número de estabelecimentos e o total de assentos** nas ruas mais movimentadas.
3.  **Comunicação dos Resultados:** Apresentar as descobertas e insights obtidos através de visualizações e conclusões textuais no notebook, além de preparar uma [apresentação em PowerPoint](https://docs.google.com/presentation/d/1Zrejz8YR0GdSlxb1B1dcN_zEUMPnMeTaDhq6OkJgqVM/edit?usp=sharing) resumindo os achados (conforme mencionado no prompt).

## Quais tecnologias usei?

Para realizar essa análise, utilizei as seguintes ferramentas e bibliotecas Python:

*   **Python:** Linguagem principal para a análise.
*   **Pandas:** Essencial para carregar (`pd.read_csv`), inspecionar (`.info()`, `.head()`), limpar (`.fillna()`, `.astype()`, `.duplicated()`, `.drop_duplicates()`, `.str.extract()`), agregar (`.groupby()`, `.value_counts()`, `.describe()`, `.mean()`) e manipular o DataFrame.
*   **NumPy:** Utilizado para otimização de tipos de dados (`np.int8`, `np.int16`) e possivelmente operações numéricas subjacentes.
*   **Matplotlib (`pyplot`) / Seaborn:** Embora Plotly Express tenha sido o principal para gráficos finais, essas bibliotecas são padrão e podem ter sido usadas para exploração inicial ou configurações de plotagem.
*   **Plotly Express (`px`):** Usado para criar gráficos interativos e visualmente informativos como histogramas (`px.histogram`), gráficos de barras (`px.bar`), violin plots (`px.violin`) e scatter plots (`px.scatter`).
*   **OS:** Para manipulação de caminhos de arquivos (`os.path.join`).
*   **Regex (via Pandas `.str.extract()`):** Para extrair informações textuais (nome da rua) dos endereços.
*   **Microsoft PowerPoint:** Para criar a apresentação final resumindo a análise e as conclusões (ferramenta externa ao notebook).

## Quais competências eu consegui?

Ao completar este sprint, demonstrei e reforcei as seguintes competências:

*   **Limpeza e Preparação de Dados:** Identifiquei e corrigi tipos de dados, tratei valores ausentes de forma apropriada para a coluna booleana 'chain', e lidei com duplicatas.
*   **Otimização de Memória:** Apliquei conversão de tipos de dados para reduzir o uso de memória do DataFrame.
*   **Engenharia de Atributos Simples:** Criei uma nova característica (`rua`) a partir de dados existentes usando extração de texto (regex).
*   **Análise Exploratória de Dados (EDA):** Utilizei uma variedade de técnicas descritivas (`.describe()`, `.value_counts()`) e visuais (`px.histogram`, `px.bar`, `px.violin`, `px.scatter`) para entender as distribuições, características e relações nos dados dos restaurantes.
*   **Análise de Segmentos:** Comparei características (como número de assentos) entre diferentes grupos (estabelecimentos de rede vs. não rede; diferentes tipos de estabelecimento).
*   **Análise Espacial Básica (por rua):** Investiguei a concentração de estabelecimentos em diferentes ruas e a relação entre densidade e capacidade (assentos).
*   **Visualização de Dados com Plotly Express:** Criei gráficos interativos e informativos para comunicar os resultados da análise de forma eficaz.
*   **Síntese e Comunicação:** Resumi as descobertas em conclusões textuais ao longo do notebook e preparei uma apresentação externa (PowerPoint) para comunicar os resultados principais.

Este sprint focou fortemente na exploração e visualização de dados para extrair insights sobre as características e a distribuição de restaurantes.