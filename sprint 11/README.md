# Sprint 11: Análise de Teste A/B (Mudança de Fonte no App)

## Qual o objetivo do sprint?

Neste sprint, meu foco foi analisar os resultados de um teste A/B realizado em um aplicativo móvel. O objetivo era determinar se a alteração da fonte tipográfica no app (testada no Grupo B) teve algum impacto significativo no comportamento dos usuários em comparação com os grupos de controle (A1 e A2, que usavam a fonte antiga). As principais etapas foram:

1.  **Carregamento e Preparação dos Dados:** Li o arquivo de logs (`logs_exp_us.csv`), renomeei as colunas, converti os tipos de dados (especialmente `time` para datetime e `group`/`event` para category para otimizar memória), e mapeei os números dos grupos para nomes mais claros ('A1', 'A2', 'B'). Verifiquei e confirmei a ausência de valores nulos.
2.  **Análise Exploratória de Dados (EDA):**
    *   Verifiquei a quantidade total de eventos e usuários únicos.
    *   Calculei a média de eventos por usuário.
    *   Analisei o período coberto pelos dados e a distribuição de eventos ao longo do tempo.
    *   Identifiquei que os dados iniciais eram incompletos e filtrei o DataFrame para considerar apenas o período com dados consistentes (a partir de 31/07/2019), calculando a pequena porcentagem de dados descartados.
    *   Verifiquei se os usuários estavam distribuídos de forma razoável entre os três grupos (A1, A2, B).
3.  **Análise do Funil de Eventos:**
    *   Identifiquei os eventos presentes e a proporção de usuários que realizaram cada um.
    *   Defini a sequência principal do funil de compras (`MainScreenAppear` -> `OffersScreenAppear` -> `CartScreenAppear` -> `PaymentScreenSuccessful`).
    *   Calculei a taxa de conversão entre cada etapa do funil, identificando onde ocorria a maior perda de usuários.
    *   Determinei a proporção de usuários que completaram todo o funil, desde a tela principal até o pagamento bem-sucedido.
4.  **Teste A/A (Validação):**
    *   Comparei os dois grupos de controle (A1 vs A2) usando testes Z para proporções para cada evento do funil.
    *   O objetivo era confirmar que não havia diferenças estatisticamente significativas entre eles, validando assim a correta divisão dos usuários e a configuração do experimento. Usei alfa = 0.1.
5.  **Teste A/B (Avaliação da Mudança):**
    *   Comparei o grupo de teste (B) com cada grupo de controle individualmente (A1 vs B, A2 vs B) e com os controles combinados (A1+A2 vs B) usando testes Z para proporções em cada etapa do funil.
    *   Usei alfa = 0.1 como nível de significância inicial.
    *   Discuti a questão dos testes múltiplos e considerei (e apliquei) um nível de significância ajustado (como Bonferroni) para controlar a taxa de erro familiar.
6.  **Conclusão:** Com base nos resultados dos testes A/A e A/B (considerando os p-valores e os níveis de significância), tirei uma conclusão sobre o impacto (ou a falta dele) da mudança de fonte no comportamento do usuário.

## Quais tecnologias usei?

Para esta análise de teste A/B, utilizei as seguintes bibliotecas e ferramentas Python:

*   **Python:** Linguagem principal para a análise.
*   **Pandas:** Para carregar (`pd.read_csv`), limpar (`.rename()`, `pd.to_datetime()`, `.astype()`, `.isnull()`), filtrar, agrupar (`.groupby()`, `.nunique()`, `.value_counts()`) e transformar os dados (`.dt.date`, `.dt.to_period()`, `.transform()`).
*   **NumPy:** Para operações numéricas, especialmente no cálculo da estatística Z e erro padrão nos testes de proporção.
*   **Matplotlib (`pyplot`) / Seaborn:** Para criar visualizações como gráficos de barras (distribuição de eventos no tempo, taxas de conversão entre etapas).
*   **SciPy (`scipy.stats`):** Fundamental para realizar os cálculos estatísticos, especificamente a função de distribuição cumulativa normal (`st.norm.cdf`) usada no cálculo do p-valor para o teste Z de proporções.
*   **OS:** Para montar o caminho do arquivo de dados (`os.path.join`).

## Quais competências eu consegui?

Completando este sprint, desenvolvi e demonstrei as seguintes competências:

*   **Análise de Testes A/B Completa:** Executei todo o processo de análise de um experimento A/B, desde a preparação dos dados até a interpretação estatística e a tomada de decisão.
*   **Pré-processamento de Dados de Log:** Limpei e estruturei dados de log, convertendo timestamps, mapeando categorias e filtrando períodos inconsistentes.
*   **Análise de Funil de Conversão:** Construí e analisei funis de eventos para identificar taxas de conversão e pontos de abandono no fluxo do usuário.
*   **Validação de Testes (A/A):** Realizei testes A/A para garantir a validade da configuração experimental e a comparabilidade dos grupos de controle.
*   **Aplicação de Testes Estatísticos (Teste Z):** Escolhi e apliquei corretamente o teste Z para comparar proporções entre grupos independentes.
*   **Interpretação de Resultados Estatísticos:** Analisei p-valores em relação a níveis de significância (alfa) e tirei conclusões sobre a significância estatística das diferenças observadas.
*   **Consciência sobre Testes Múltiplos:** Reconheci o problema da inflação do erro Tipo I ao realizar múltiplos testes e compreendi a necessidade (e aplicação básica) de métodos de correção como Bonferroni.
*   **Visualização de Dados para Análise:** Criei gráficos para explorar a distribuição temporal e as taxas de conversão do funil.
*   **Comunicação Clara de Resultados:** Elaborei uma conclusão detalhada explicando os passos da análise, os resultados estatísticos e as implicações para a decisão de negócio (manter ou não a nova fonte).

Este sprint foi uma aplicação prática importante de estatística inferencial e análise de funil para avaliar o impacto de uma mudança de produto em um ambiente de teste controlado.