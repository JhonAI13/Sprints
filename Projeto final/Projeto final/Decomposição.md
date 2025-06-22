# Plano de Ação Detalhado para o Projeto de Teste A/B

Este plano detalha as etapas necessárias para completar a análise do teste A/B, seguindo a descrição da tarefa e expandindo os pontos de verificação.

## 1. Objetivos do Estudo

- [x] Descrever o objetivo principal: Testar se o novo sistema de recomendação melhora a conversão dos usuários nas etapas especificadas do funil.
- [x] Definir a hipótese nula (H₀) e a hipótese alternativa (H₁):
    - [x] H₀: Não há diferença estatisticamente significativa na conversão entre o grupo A (controle) e o grupo B (novo sistema) em nenhuma das etapas do funil (`product_page`, `product_cart`, `purchase`).
    - [x] H₁: O grupo B tem uma taxa de conversão estatisticamente maior que o grupo A em pelo menos uma das etapas do funil (`product_page`, `product_cart`, `purchase`).
- [x] Declarar o critério de sucesso esperado: Atingir um aumento de pelo menos 10% nas taxas de conversão para `product_page`, `product_cart` e `purchase` para o grupo B, em comparação com o grupo A, dentro de 14 dias após o cadastro do usuário.

## 2. Exploração e Preparação dos Dados

- [x] Carregar os dados:
    - [x] `ab_project_marketing_events_us.csv`
    - [x] `final_ab_new_users_upd_us.csv`
    - [x] `final_ab_events_upd_us.csv`
    - [x] `final_ab_participants_upd_us.csv`
- [x] Verificar e corrigir tipos de dados:
    - [x] Converter colunas de data/hora.
- [x] Tratar dados ausentes e duplicados:
    - [x] Verificar cada DataFrame em busca de valores nulos (`.isnull().sum()`) e decidir a estratégia de tratamento (se necessário, remover ou preencher, justificando a escolha).
    - [x] Verificar duplicatas explícitas (`.duplicated().sum()`) em cada DataFrame.
    - [x] Verificar se algum `user_id` aparece em mais de um grupo de teste no DataFrame `final_ab_participants_upd_us.csv`. Se sim, remover esses usuários.
- [x] **Verificação de consistência do Teste (Etapa Crítica!)**:
    - [x] **Público-alvo vs. Dados:** Documentar a inconsistência entre a descrição técnica ("região da UE") e os nomes dos arquivos ("_us.csv", indicando EUA). Prosseguir com a análise nos dados dos EUA, mas destacar essa discrepância nas conclusões.
    - [x] **Período de recrutamento:** Filtrar os usuários do `final_ab_new_users_upd_us.csv` para incluir apenas aqueles com `first_date` entre 07-12-2020 e 21-12-2020 (inclusive).
    - [x] **Período de eventos:** Filtrar os eventos do `final_ab_events_upd_us.csv` para incluir apenas aqueles que ocorreram até 01-01-2021 (inclusive) e que pertencem aos usuários recrutados no período correto.
    - [x] **Período de análise pós-cadastro:** Filtrar os eventos de cada usuário para considerar apenas aqueles que ocorreram dentro de 14 dias após a sua `first_date`.
    - [x] **Número de participantes:** Verificar o número total de usuários únicos no DataFrame `final_ab_participants_upd_us.csv` para o teste `recommender_system_test` e comparar com o número esperado (6000).
    - [x] **Filtrar participantes relevantes:** Cruzar os dados de usuários recrutados, eventos e participantes para garantir que apenas os usuários que participaram do teste `recommender_system_test` (presentes em `final_ab_participants_upd_us.csv` para esse teste) e que se cadastraram no período correto (`final_ab_new_users_upd_us.csv`) sejam incluídos na análise.
    - [x] Garantir que todos os usuários incluídos na análise pertencem a um (e apenas um) grupo do teste `recommender_system_test`.

## 3. Análise Exploratória de Dados (AED)

- [x] Distribuição dos participantes:
    - [x] Verificar a divisão de usuários entre os grupos A e B após todos os filtros de consistência. Avaliar se a divisão é razoavelmente igual.
    - [x] Analisar a distribuição dos usuários nos grupos A e B por `region` e `device`. Verificar se há diferenças substanciais que possam enviesar os resultados.
- [x] Análise do Funil de Eventos
- [x] Distribuição de Eventos ao Longo do Tempo:
    - [x] Criar um gráfico mostrando o número total de eventos por dia ao longo do período do teste (07-12-2020 a 01-01-2021).
    - [x] Opcional, mas recomendado: Sobrepor as datas dos eventos de marketing (`ab_project_marketing_events_us.csv`) neste gráfico para ver se houve influência no volume de eventos.
    - [x] Analisar a distribuição diária de eventos *por grupo* (A e B) para verificar se há padrões ou anomalias em dias específicos que afetem um grupo mais do que o outro.

## 4. Avaliação dos Resultados do Teste A/B

- [x] Preparar dados para o teste Z:
    - [x] Para cada etapa do funil que será testada (`product_page`, `product_cart`, `purchase`), agregar os dados para obter:
        - [x] Número de usuários no grupo A que realizaram o evento (sucessos).
        - [x] Número de usuários no grupo B que realizaram o evento (sucessos).
- [x] Executar o teste Z de proporção:
    - [x] Definir um nível de significância (alfa), por exemplo, `alpha = 0.05`.
    - [x] Realizar um teste Z de proporção unilateral (se a hipótese é de *aumento*) ou bilateral (se é apenas *diferença*) para cada uma das três etapas do funil (`product_page`, `product_cart`, `purchase`) comparando o grupo B vs. o grupo A.
    - [x] Comparar o p-valor obtido com o alfa para determinar se a diferença observada na conversão entre os grupos é estatisticamente significativa para cada etapa.
    - [x] **Atenção:** Considerar o problema das comparações múltiplas ao realizar testes separados para cada etapa do funil. Mencionar essa limitação ou aplicar uma correção (ex: Bonferroni) se o tempo/escopo permitir e for metodologicamente adequado para funis sequenciais.
- [x] Interpretar os resultados:
    - [x] Para cada etapa do funil, declarar se a diferença de conversão entre A e B foi estatisticamente significativa ao nível de alfa escolhido.
    - [x] Calcular a diferença percentual relativa na conversão para cada etapa (`(Conversão_B - Conversão_A) / Conversão_A`). O grupo B alcançou o aumento esperado de 10% em relação ao grupo A?

