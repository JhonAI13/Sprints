# Projeto de Análise de Churn e Segmentação de Clientes - Academia "Model Fitness"

## Visão Geral do Projeto

Este projeto tem como foco principal a análise da rotatividade de clientes (churn) na academia "Model Fitness", utilizando o conjunto de dados `gym_churn_us.csv`. O objetivo é desvendar as causas da evasão de clientes, segmentá-los em perfis característicos e, a partir desses insights, propor recomendações estratégicas para mitigar o churn e aprimorar a experiência geral do cliente.

## Objetivo

*   **Identificar Preditores de Churn:** Entender quais características e comportamentos dos clientes estão mais associados à decisão de cancelar a afiliação.
*   **Construir Modelos Preditivos:** Desenvolver e avaliar modelos de Machine Learning capazes de prever a probabilidade de um cliente evadir.
*   **Segmentar Clientes:** Agrupar clientes em perfis distintos para uma compreensão mais aprofundada de suas necessidades e riscos de churn.
*   **Formular Recomendações Estratégicas:** Propor ações direcionadas para reter clientes, com base nas análises de churn e segmentação.

## Metodologia

A abordagem metodológica seguiu as seguintes etapas:

1.  **Carregamento e Pré-processamento de Dados:**
    *   Leitura do dataset `gym_churn_us.csv`.
    *   Renomeação de colunas para o português (`mapa_colunas_ptbr`).
    *   Otimização de tipos de dados para reduzir o uso de memória, convertendo colunas binárias/categóricas para `int8`.
2.  **Análise Exploratória de Dados (EDA):**
    *   Análise descritiva das variáveis (df.describe()).
    *   Comparação das características entre grupos de clientes que evadiram (Churn=1) e os que permaneceram (Churn=0) através de médias e distribuições (KDE plots para numéricas e Count plots para categóricas).
    *   Criação e análise da matriz de correlação para identificar relações entre as variáveis e a variável alvo (`evasao`), bem como a multicolinearidade.
3.  **Modelagem Preditiva (Previsão de Churn):**
    *   Seleção de features relevantes para o modelo preditivo, evitando variáveis altamente correlacionadas.
    *   Divisão dos dados em conjuntos de treino e teste (`train_test_split`), com estratificação para manter a proporção da classe alvo.
    *   Treinamento e avaliação de dois modelos de classificação: Regressão Logística e Random Forest Classifier.
    *   Comparação das métricas de desempenho: Acurácia, Precisão e Recall.
4.  **Clusterização de Clientes:**
    *   Padronização das features numéricas utilizando `StandardScaler`.
    *   Construção de um dendrograma para auxiliar na determinação do número ideal de clusters.
    *   Aplicação do algoritmo K-Means para segmentar os clientes em 5 clusters.
    *   Análise das características médias de cada cluster para definir seus perfis.
    *   Visualização das distribuições das características por cluster para confirmar as diferenciações.
    *   Cálculo da taxa de evasão (churn) para cada cluster.
5.  **Análise e Recomendações:**
    *   Interpretação dos perfis de cluster identificados e suas respectivas taxas de churn.
    *   Desenvolvimento de recomendações acionáveis e direcionadas para retenção de clientes, com base nos insights obtidos.

## Ferramentas e Bibliotecas

O projeto foi desenvolvido em um ambiente Jupyter Notebook e utilizou as seguintes bibliotecas Python:

*   **`pandas`**: Para manipulação e análise de dados.
*   **`numpy`**: Para operações numéricas.
*   **`matplotlib.pyplot`**: Para visualização estática de dados.
*   **`seaborn`**: Para visualização estatística de dados, construído sobre Matplotlib.
*   **`plotly.express`**: Para visualizações interativas (embora não tenha sido utilizado em plots neste notebook, foi importado).
*   **`os`**: Para manipulação de caminhos de arquivo.
*   **`scipy.stats`**: Para funções estatísticas.
*   **`scipy.cluster.hierarchy`**: Para análise hierárquica e construção de dendrogramas.
*   **`sklearn.preprocessing.StandardScaler`**: Para padronização de dados.
*   **`sklearn.decomposition.PCA`**: Para Análise de Componentes Principais (importado, mas não utilizado explicitamente em uma etapa final do notebook).
*   **`sklearn.model_selection.train_test_split`**: Para dividir dados em conjuntos de treino e teste.
*   **`sklearn.linear_model.LogisticRegression`**: Para o modelo de Regressão Logística.
*   **`sklearn.ensemble.RandomForestClassifier`**: Para o modelo de Random Forest.
*   **`sklearn.metrics`**: Para avaliação do desempenho dos modelos (accuracy_score, precision_score, recall_score).
*   **`sklearn.cluster.KMeans`**: Para o algoritmo de clusterização K-Means.

## Análise e Resultados Principais

### Análise Exploratória de Dados (EDA)

*   O dataset continha 7 colunas, sem valores nulos.
*   A taxa de churn (evasão) foi de 26.5%, indicando um desbalanceamento de classes.
*   **Clientes que evadem (Churn=1)** se diferenciam por:
    *   **Menor permanência e contratos curtos:** Drasticamente menores `duracao_contrato_meses`, `meses_fim_contrato` e `tempo_cliente_meses` (concentrados nos primeiros meses).
    *   **Menor engajamento:** Frequência de visitas (`media_freq_semanal_total` e `media_freq_semanal_mes`) muito mais baixa. Menos propensos a serem parceiros de empresa, vir de promoções de amigos ou participar de visitas em grupo.
    *   **Menor gasto:** Gastam menos em serviços extras.
*   **Variáveis menos relevantes:** `sexo` e `telefone_fornecido` apresentaram pouca diferença entre os grupos.
*   **Correlações:** `tempo_cliente_meses`, `idade`, `media_freq_semanal_mes`, `duracao_contrato_meses` e `meses_fim_contrato` mostraram as correlações negativas mais fortes com a evasão, confirmando serem os principais preditores. Identificada alta multicolinearidade entre `duracao_contrato_meses` e `meses_fim_contrato`, e entre `media_freq_semanal_total` e `media_freq_semanal_mes`.

### Modelagem Preditiva (Churn)

*   Foram treinados e avaliados modelos de Regressão Logística e Random Forest para prever a evasão.
*   **Regressão Logística** superou o Random Forest em todas as métricas:
    *   **Acurácia:** 0.9150
    *   **Precisão:** 0.8600
    *   **Recall:** 0.8113
*   A Regressão Logística, sendo um modelo mais simples, demonstrou ser mais eficaz para este problema, indicando que a relação entre as features e o churn pode ser bastante linear.

### Clusterização de Clientes

O K-Means, após análise do dendrograma, agrupou os clientes em 5 perfis distintos:

*   **Cluster 0 (Jovens e Novos, Baixo Engajamento/Uso/Gasto):**
    *   **Perfil:** Idade mais jovem, baixíssimos gastos extras, contratos muito curtos (pico em 1 mês), menor tempo de cliente, baixa frequência de visitas, menor participação em programas de parceria/promoção/grupo.
    *   **Risco de Evasão:** **MUITO ALTO (maior taxa de evasão)**.
*   **Cluster 1 (Leais e Engajados - IDEAL):**
    *   **Perfil:** Idade intermediária, gastos extras moderados, contratos longos, tempo de cliente e frequência moderados/altos, alta participação em programas de parceria/promoção/grupo.
    *   **Risco de Evasão:** **MUITO BAIXO (segunda menor taxa de evasão)**.
*   **Cluster 2 (Frequentes, Baixo Gasto Extra, Contratos Curtos):**
    *   **Perfil:** Idade intermediária, gastos extras mais baixos, contratos mais curtos (mas não como o Cluster 0), tempo de cliente relativamente novo, alta frequência de visitas, participação em programas de parceria/promoção/grupo.
    *   **Risco de Evasão:** **INTERMEDIÁRIO (moderado)**. São ativos, mas menos "presos" por contratos longos.
*   **Cluster 3 (Altamente Leais e Antigos):**
    *   **Perfil:** Mais velhos, gastos extras moderados/altos, contratos longos, **maior tempo de cliente**, frequência moderada/alta, alta participação em programas de parceria/promoção/grupo.
    *   **Risco de Evasão:** **BAIXÍSSIMO (a menor taxa de evasão)**. O grupo dos "veteranos" da academia.
*   **Cluster 4 (Alto Gasto, Contratos Curtos, Baixo Engajamento):**
    *   **Perfil:** Mais jovens, **gastos extras significativamente mais altos**, contratos curtos, menor tempo de cliente, baixa frequência de visitas, baixa participação em programas de parceria/promoção/grupo.
    *   **Risco de Evasão:** **ALTO ("Silencioso")**. Gastam muito em extras, mas o engajamento com a atividade principal e os vínculos sociais são baixos, indicando fragilidade.

## Conclusões e Recomendações

A retenção de clientes na "Model Fitness" está intrinsecamente ligada à **duração do contrato** e ao **nível de engajamento** dos membros. Clientes com contratos mais curtos e menor participação nas atividades e na comunidade da academia (especialmente os perfis "Jovens e Novos" - Cluster 0, e "Alto Gasto, Contratos Curtos, Baixo Engajamento" - Cluster 4) são os que mais evadem. Em contrapartida, clientes leais tendem a ter contratos mais longos e um engajamento robusto.

### Recomendações Estratégicas para Interação e Retenção:

1.  **Personalização da Comunicação:**
    *   **Para Clientes de Alto Risco (Cluster 0 e 4):** Focar em comunicação que destaque os benefícios de longo prazo da academia, os diferentes tipos de aulas/serviços e testemunhos de clientes satisfeitos.
    *   **Para Clientes Leais (Cluster 1 e 3):** Reconhecer e recompensar a lealdade, solicitando feedback para aprimorar a experiência e incentivando a indicação de novos membros.
2.  **Fortalecimento do Senso de Comunidade:**
    *   **Foco no Cluster 0 e 4:** Incentivar a participação em aulas/eventos em grupo (Zumba, Yoga, etc.), que demonstraram ser um fator de retenção. Criar desafios internos ou programas de "amigo da academia".
    *   **Onboarding Aprimorado:** Para novos membros, especialmente do Cluster 0, oferecer sessões de orientação personalizadas, introduzir a instrutores e outros membros, e acompanhar o progresso inicial para garantir que se sintam acolhidos e engajados desde o começo.
3.  **Incentivo a Contratos Mais Longos:**
    *   **Para Cluster 0, 2 e 4:** Oferecer descontos progressivos ou benefícios adicionais (ex: acesso a áreas exclusivas, aulas premium) para clientes que optarem por contratos de 6 ou 12 meses.
    *   **Estratégias de Renovação:** Próximo ao final do contrato, especialmente para o Cluster 2 e 4, abordar proativamente os clientes com ofertas de renovação atrativas e personalizadas, destacando o valor e os benefícios de continuar.
4.  **Monitoramento Proativo do Engajamento:**
    *   Utilizar os modelos preditivos para identificar clientes com alta probabilidade de churn (especialmente aqueles do Cluster 0 e 4) antes que tomem a decisão de sair.
    *   Implementar um sistema de alerta para baixa frequência de visitas ou queda no uso de serviços extras.
    *   Com base nesses alertas, a equipe da academia pode realizar contato proativo (telefone, e-mail) para entender a situação do cliente e oferecer suporte ou soluções personalizadas.
5.  **Programas de Fidelidade:**
    *   Criar um programa de pontos ou níveis que recompense não apenas a permanência, mas também a frequência de visitas e o uso de diversos serviços.
    *   Essas recompensas podem incluir meses grátis, acesso a workshops exclusivos, produtos da academia, ou créditos para serviços adicionais.

## Próximos Passos e Melhorias Futuras

*   **Engenharia de Features:**
    *   Explorar a criação de novas features a partir das existentes (ex: proporção de `gastos_extras_total` por `tempo_cliente_meses`).
    *   Testar a combinação de variáveis correlacionadas para simplificar o modelo e potencialmente melhorar o desempenho.
*   **Otimização de Modelos Preditivos:**
    *   Realizar ajuste de hiperparâmetros (Hyperparameter Tuning) para a Regressão Logística e Random Forest (ex: usando GridSearchCV ou RandomizedSearchCV) para extrair o máximo de desempenho.
    *   Considerar o uso de técnicas para lidar com o desbalanceamento de classes (ex: SMOTE, ajuste de pesos das classes nos modelos) para melhorar o Recall para a classe "evasão".
*   **Exploração de Outros Modelos:**
    *   Testar modelos mais avançados, como Gradient Boosting (XGBoost, LightGBM) ou Support Vector Machines (SVMs), que podem capturar relações não lineares complexas.
*   **Análise de Custo-Benefício:**
    *   Integrar uma análise de custo-benefício para as recomendações de retenção, estimando o ROI de cada ação para a academia.
*   **Feedback e Acompanhamento:**
    *   Implementar um sistema para coletar feedback contínuo dos clientes e monitorar a eficácia das estratégias de retenção ao longo do tempo.