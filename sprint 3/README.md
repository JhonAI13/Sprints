# Sprint 3: Análise de Pedidos da Instacart

## Qual o objetivo do sprint?

Neste sprint, mergulhei no conjunto de dados de pedidos do Instacart, que estava dividido em várias tabelas (`instacart_orders.csv`, `products.csv`, `aisles.csv`, `departments.csv`, `order_products.csv`). O objetivo principal era realizar uma análise completa, começando pela **visão geral dos dados** para entender a estrutura e o conteúdo de cada tabela. Em seguida, a meta foi **preparar os dados**, o que envolveu:

1.  Verificar e corrigir os tipos de dados das colunas (garantindo que IDs fossem numéricos, datas fossem datetime, etc.).
2.  Identificar e tratar **valores ausentes**, principalmente na coluna `days_since_prior_order`, entendendo por que eles ocorriam (primeiro pedido do cliente).
3.  Encontrar e lidar com **valores duplicados**, se existissem, para garantir a integridade dos dados.
4.  Finalmente, realizar uma **Análise Exploratória de Dados (EDA)** para descobrir padrões no comportamento de compra dos clientes, como os horários e dias da semana mais populares para pedidos, o tempo entre pedidos e os produtos mais frequentemente comprados ou recomprados.

## Quais tecnologias usei?

Para realizar essa análise abrangente, utilizei as seguintes ferramentas e bibliotecas Python:

*   **Python:** Como linguagem principal para todo o processo.
*   **Pandas:** Essencial para carregar os múltiplos arquivos CSV (`pd.read_csv`), inspecionar (`.info()`, `.head()`, `.describe()`), limpar (`.isnull().sum()`, `.fillna()`, `.duplicated().sum()`, `.drop_duplicates()`, `.astype()`), mesclar (`pd.merge`) e agregar (`.groupby()`, `.value_counts()`) os dados das diferentes tabelas.
*   **NumPy:** Provavelmente utilizada para operações numéricas, especialmente em conjunto com Pandas.
*   **Matplotlib (`pyplot`):** Para criar as visualizações necessárias na etapa de EDA, como histogramas (distribuição de pedidos por hora, dias desde o último pedido) e gráficos de barras (pedidos por dia da semana, produtos populares).

## Quais competências eu consegui?

Ao concluir este sprint, demonstrei e aprimorei as seguintes competências:

*   **Manipulação de Múltiplas Fontes de Dados:** Carreguei, inspecionei e combinei informações de cinco tabelas diferentes usando Pandas, compreendendo as relações entre elas através das chaves (IDs).
*   **Limpeza e Preparação de Dados:** Apliquei técnicas robustas para identificar e corrigir problemas de qualidade de dados, incluindo tratamento de valores ausentes (com justificativa baseada no contexto do negócio), verificação e remoção de duplicatas, e correção de tipos de dados.
*   **Análise Exploratória de Dados (EDA):** Realizei análises descritivas e visuais para entender padrões de compra dos clientes, como picos de horários e dias, frequência de pedidos e produtos mais relevantes.
*   **Visualização de Dados:** Criei gráficos (histogramas, barras) com Matplotlib para comunicar efetivamente os padrões encontrados nos dados.
*   **Pensamento Crítico e Resolução de Problemas:** Analisei a causa dos valores ausentes e duplicatas (quando encontrados) e escolhi métodos apropriados para tratá-los, justificando minhas decisões.
*   **Trabalho com Dados Relacionais:** Utilizei `pd.merge` para juntar informações de diferentes tabelas, permitindo análises mais complexas que envolviam dados de produtos, pedidos e clientes.

Este sprint foi fundamental para praticar o fluxo completo de pré-processamento e EDA em um cenário com múltiplas tabelas relacionadas, um desafio comum em análise de dados.