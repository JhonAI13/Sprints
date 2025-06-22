Análise e Recomendação Estratégica para Lances de Anúncios no Facebook
Objetivo Principal do Analista: Conduzir uma análise rigorosa de um teste A/B para determinar a performance comparativa das estratégias de "lance médio" e "lance máximo" do Facebook em relação a métricas de engajamento (Cliques/CTR) e conversão (Compras/Taxa de Conversão de Compra), avaliando a significância estatística das diferenças encontradas para embasar uma recomendação estratégica.

Dataset

Decomposição da Tarefa (Perspectiva do Analista de Dados):

Entendendo o Projeto e Definindo Escopo
Confirmação do Objetivo de Negócio: Assegurar que a meta primária é identificar a estratégia de lance mais eficaz para maximizar Cliques e Compras.
Identificação dos Stakeholders: Entender quem utilizará os resultados (Provavelmente: Equipe de Marketing/Performance).
Decisão a ser Suportada: A análise deve fornecer uma base sólida para a decisão sobre qual estratégia de lance adotar em campanhas futuras.
Validação do Dataset e Necessidade de Confirmação da Coluna de Grupo (Ponto Crítico!):
Ação: Acessar o dataset (via link ou descrição).
Verificação: Crucialmente, confirmar a existência e clareza de uma coluna que categorize cada linha de dados como pertencente ao grupo de "controle" (lance máximo, assumindo como padrão ou ponto de comparação) ou "teste" (lance médio).
Plano B (se ausente): Se a coluna não existir ou não for clara, pausar e buscar esclarecimento com a fonte dos dados sobre como os grupos foram registrados ou se há outra forma de distingui-los. Esta informação é mandatória para a análise A/B.
Preparação dos Dados (Pré-processamento)
Carregamento do Dataset: Importar os dados para o ambiente de análise (Ex: Pandas no Python).
Avaliação e Tratamento de Valores Ausentes (Missing Values):
Ação: Verificar a presença de NaN ou outros indicadores de valores ausentes nas col colunas chave (Impression, Click, Purchase, Earnings, e a coluna de grupo).
Decisão/Estratégia: Documentar e aplicar a estratégia de tratamento (Ex: Remoção de linhas se poucos dados faltantes e não impactar a representatividade; Imputação apenas se justificada e com cuidado para não distorcer a análise - provável remoção neste caso de métricas de performance).
Verificação de Tipos de Dados:
Ação: Confirmar se Impression, Click, Purchase, Earnings estão como tipos numéricos adequados (inteiro ou float).
Ação: Confirmar se a coluna de grupo é categórica (object ou category). Corrigir se necessário.
Identificação e Remoção de Duplicatas:
Ação: Verificar se há linhas completamente duplicadas que possam inflar artificialmente o tamanho da amostra.
Ação: Remover duplicatas se encontradas, documentando o número de linhas removidas.
Padronização/Verificação dos Nomes das Colunas: Assegurar que os nomes das colunas estão consistentes e fáceis de referenciar no código.
Confirmação e Criação da Coluna de Grupo: Assegurar que, após o pré-processamento, existe uma coluna binária ou categórica clara identificando 'Controle' ("lance máximo") e 'Teste' ("lance médio"). Renomear se necessário para clareza (Ex: Strategy, Group, TestGroup).
Exploração e Análise Descritiva (EDA)
Cálculo de Estatísticas Descritivas por Grupo:
Ação: Utilizar groupby() na coluna de grupo para calcular média, mediana, desvio padrão, min, max, quartis para Impression, Click, Purchase, Earnings separadamente para cada estratégia.
Objetivo: Obter um primeiro panorama da performance de cada grupo e identificar possíveis discrepâncias iniciais ou outliers.
Visualização das Distribuições:
Ação: Criar histogramas e boxplots para Impression, Click, Purchase, Earnings para cada grupo.
Objetivo: Visualizar a forma das distribuições, identificar outliers e entender a variabilidade dos dados dentro de cada grupo.
Cálculo de Métricas Derivadas Chave:
Ação: Calcular para cada linha/registro (ou agregado por grupo, dependendo da estrutura do dado):
Taxa de Cliques (CTR) = Click / Impression
Taxa de Conversão (Click -> Compra) = Purchase / Click (Gerenciar divisão por zero onde Click é 0)
Ganhos por Compra = Earnings / Purchase (Gerenciar divisão por zero onde Purchase é 0)
Ganhos por Clique = Earnings / Click (Gerenciar divisão por zero onde Click é 0)
Tratamento de Divisão por Zero: Decidir como tratar casos onde o denominador é zero (Ex: Atribuir 0 ou NaN; remover da métrica agregada). Documentar a abordagem.
Comparação Visual das Métricas Derivadas:
Ação: Criar gráficos de barras ou outros visuais comparando a média (ou mediana) das métricas derivadas (CTR, Taxa de Conversão, etc.) entre os grupos "lance médio" e "lance máximo".
Objetivo: Ter uma prévia visual das diferenças de performance nas métricas de negócio cruciais.
Definição das Hipóteses Estatísticas
Formalização das Hipóteses: Estabelecer claramente as hipóteses Nula (H0) e Alternativa (H1) para as principais métricas de comparação, que serão testadas estatisticamente.
Para Cliques / CTR:
H0: Não há diferença estatisticamente significativa na média de Cliques (ou CTR) entre "lance médio" e "lance máximo".
H1: Há uma diferença estatisticamente significativa na média de Cliques (ou CTR) entre as estratégias.
Para Compras / Taxa de Conversão:
H0: Não há diferença estatisticamente significativa na média de Compras (ou Taxa de Conversão) entre "lance médio" e "lance máximo".
H1: Há uma diferença estatisticamente significativa na média de Compras (ou Taxa de Conversão) entre as estratégias.
Para Ganhos (Opcional/Adicional):
H0: Não há diferença estatisticamente significativa na média de Ganhos entre "lance médio" e "lance máximo".
H1: Há uma diferença estatisticamente significativa na média de Ganhos entre as estratégias.
Realização dos Testes Estatísticos (Teste A/B Formal)
Seleção dos Testes Adequados:
Ação: Para comparar proporções (CTR, Taxa de Conversão): Utilizar Teste Z para Duas Proporções ou Teste Qui-Quadrado (dependendo da estrutura dos dados - se agregado ou por evento).
Ação: Para comparar médias (Cliques, Compras, Ganhos):
Verificação de Premissas: Antes de aplicar o teste t, verificar a normalidade (Ex: Teste de Shapiro-Wilk, análise visual dos histogramas) e a homogeneidade das variâncias (Ex: Teste de Levene) para cada grupo.
Aplicação: Se as premissas forem razoavelmente atendidas, usar o Teste t de Student para amostras independentes. Se as premissas não forem atendidas (especialmente normalidade em amostras pequenas ou médias), considerar o Teste Não Paramétrico de Mann-Whitney U.
Definição do Nível de Significância (Alfa):
Ação: Fixar α = 0.05 como o limite para rejeição da H0.
Execução dos Testes:
Ação: Aplicar os testes estatísticos selecionados para cada par de grupo/métrica (Clique/CTR, Compra/Taxa de Conversão, Ganhos).
Cálculo e Interpretação do p-valor:
Ação: Obter o p-valor resultante de cada teste.
Interpretação:
Se p-valor < 0.05: Rejeitar H0. Concluir que há evidência estatística forte de uma diferença real entre as estratégias para aquela métrica.
Se p-valor ≥ 0.05: Não rejeitar H0. Concluir que não há evidência estatística suficiente nos dados para afirmar que existe uma diferença real entre as estratégias para aquela métrica.
Análise de Impacto de Negócio
Quantificação do "Lift" (Ganho/Perda Percentual):
Ação: Calcular a diferença percentual ou absoluta nas métricas chave (média/taxa) entre o grupo de teste ("lance médio") e o grupo de controle ("lance máximo").
Exemplo: Lift % = ((Métrica_Teste - Métrica_Controle) / Métrica_Controle) * 100.
Análise da Significância Prática vs. Estatística:
Ação: Avaliar se a magnitude das diferenças encontradas (o "lift"), mesmo que estatisticamente significativas, é relevante do ponto de vista de negócio. Uma diferença de 0.1% no CTR pode ser significativa estatisticamente em grandes amostras, mas irrelevante na prática.
Consideração: Levar em conta os custos associados a cada estratégia de lance (embora não estejam explicitamente nos dados, é um fator de negócio).
Síntese, Recomendações e Próximos Passos
Compilação dos Resultados: Sumarizar as principais descobertas da EDA e os resultados dos testes de hipóteses (incluindo p-valores e "lift").
Criação de Visualizações Conclusivas: Desenvolver gráficos e tabelas claros que comparem diretamente as métricas e os resultados estatísticos entre os grupos.
Resposta às Questões de Negócio: Articular claramente qual estratégia performou melhor para Cliques e Compras, e se essa diferença é estatisticamente confiável.
Recomendação: Fornecer uma recomendação clara e baseada nos dados para a equipe de marketing sobre qual estratégia de lance adotar para futuras campanhas, justificando a escolha com base na análise.
Documentação de Limitações e Sugestões:
Ação: Identificar quaisquer limitações inerentes ao estudo (Ex: Duração do teste, tamanho da amostra, ausência de dados de custo, outras variáveis não controladas).
Ação: Sugerir possíveis próximos passos ou testes futuros para obter insights mais aprofundados (Ex: Testar outras estratégias, segmentar a análise por tipo de criativo, incluir dados de custo/ROI).
Potencialização com Dashboard (Opcional - se aplicável e houver tempo/requerimento)
Planejamento do Dashboard:
Ação: Identificar as métricas e visualizações mais importantes para acompanhar a performance contínua das campanhas e comunicar os resultados do A/B de forma acessível.
Conteúdo Sugerido: Comparativos de CTR, Taxa de Conversão, Cliques, Compras por estratégia; Gráficos de tendência ao longo do tempo (se os dados permitirem); Resumo dos resultados do teste A/B (lift, indicação de significância).
Desenvolvimento no Tableau: Construir o dashboard com as visualizações planejadas.
Click to add a cell.