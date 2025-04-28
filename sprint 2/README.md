# Sprint 2: Análise de Dados de Streaming de Música (Yandex Music)

## Qual o objetivo do sprint?

Neste sprint, o foco foi analisar dados de uso do serviço de streaming Yandex Music. O objetivo principal era **comparar o comportamento dos usuários** das cidades de Springfield e Shelbyville. Para isso, precisei:

1.  **Pré-processar os dados:** Carregar a tabela, inspecionar as colunas, verificar e corrigir tipos de dados, encontrar e tratar valores ausentes (como nomes de faixas ou artistas), identificar e remover duplicatas (explícitas e implícitas), e padronizar possíveis inconsistências nos nomes (como gêneros musicais).
2.  **Testar hipóteses:** Formular e testar hipóteses específicas sobre as diferenças nos padrões de escuta entre as duas cidades em determinados dias da semana (segundas e sextas-feiras). O objetivo era verificar se a atividade musical dos usuários variava significativamente entre as cidades nesses dias.

## Quais tecnologias usei?

Para realizar essa análise, utilizei as seguintes tecnologias e bibliotecas Python:

*   **Python:** Linguagem base para toda a manipulação e análise.
*   **Pandas:** Fundamental para carregar os dados (`pd.read_csv`), explorar (`.info()`, `.head()`, `.describe()`, `.value_counts()`), limpar (tratamento de nulos com `.fillna()`, remoção de duplicatas com `.duplicated()` e `.drop_duplicates()`), filtrar e agrupar os dados (`.groupby()`, boolean indexing).
*   **SciPy (`scipy.stats`):** Utilizada para realizar os testes de hipóteses estatísticas (provavelmente um teste t para comparar as médias ou proporções de escuta entre os grupos).

*(Observação: Embora não explicitamente detalhado no notebook original, ferramentas de visualização como Matplotlib ou Seaborn poderiam ter sido usadas para gráficos exploratórios, mas o foco principal foi o pré-processamento e o teste de hipóteses).*

## Quais competências eu consegui?

Ao finalizar este sprint, desenvolvi e demonstrei as seguintes competências:

*   **Pré-processamento de Dados:** Identificação e tratamento eficaz de problemas comuns em dados reais, como valores ausentes, duplicatas (explícitas e implícitas), tipos de dados incorretos e inconsistências textuais.
*   **Análise Exploratória de Dados (EDA):** Capacidade de investigar um conjunto de dados para entender sua estrutura, distribuições e identificar padrões iniciais ou anomalias.
*   **Manipulação de Dados com Pandas:** Habilidade em filtrar, agrupar, agregar e transformar dados para preparar a análise e responder a perguntas específicas.
*   **Teste de Hipóteses Estatísticas:** Compreensão e aplicação prática do processo de teste de hipóteses:
    *   Formulação de hipóteses nula (H₀) e alternativa (H₁).
    *   Escolha de um teste estatístico apropriado.
    *   Definição de um nível de significância (alfa).
    *   Cálculo e interpretação do p-valor.
    *   Tomada de decisão estatística (rejeitar ou não H₀).
*   **Resolução de Problemas Orientada a Dados:** Utilização de técnicas de análise de dados para investigar e responder a uma questão de negócio sobre o comportamento do usuário em diferentes contextos (cidades e dias da semana).
*   **Comunicação de Resultados:** Capacidade de explicar o processo de análise e as conclusões de forma clara e concisa.

Este sprint foi essencial para praticar a limpeza de dados e a aplicação de testes estatísticos para tirar conclusões baseadas em evidências.