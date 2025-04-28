# Repositório Sprints - Projetos de Análise de Dados

Este repositório contém uma coleção de Jupyter Notebooks (`.ipynb`), scripts Python (`.py`), apresentações (`.pptx`) e arquivos de dados correspondentes, organizados em sprints de análise de dados e exercícios. Cada sprint numerado é dedicado a um projeto específico, abrangendo diversas etapas do processo de análise, desde a limpeza e preparação dos dados até a análise exploratória (AED) e testes de hipóteses estatísticas. O diretório `Ex` contém notebooks de exercícios focados em técnicas específicas.

## Estrutura do Repositório

O repositório está organizado nos seguintes diretórios:

*   **`Sprints`**: Diretório raiz contendo este arquivo `README.md` e subdiretórios para cada sprint e exercícios.
    *   **`Ex`**: Contém notebooks com exercícios práticos sobre técnicas específicas de análise de dados.
        *   `Coorte.ipynb`: Exercício de análise de coorte usando Pandas.
        *   `groupby.ipynb`: Exercícios de aplicação do método `groupby` do Pandas.
        *   `plotly.ipynb`: Exercícios de visualização de dados com Plotly (gráficos de barra, pizza, funil).
    *   **`sprint 1`**: Avaliação e preparação de dados de clientes de e-commerce. Sprint introdutório com foco em qualidade e limpeza de dados.
        *   `sprint 1.ipynb`: Notebook focado na limpeza e preparação de dados de e-commerce.
    *   **`sprint 3`**: Análise de dados de pedidos da Instacart. Projeto com foco em visão geral dos dados, tratamento de duplicatas e valores ausentes, e AED de dados de supermercado online.
        *   `078eb029-d762-4f21-8c07-bfb555d6a3e9.ipynb`: Notebook para análise de pedidos da Instacart.
        *   `datasets`: Subdiretório contendo os datasets utilizados.
    *   **`sprint 4`**: Análise de planos de telecomunicações da Megaline. Projeto que explora pré-processamento, agregação de dados, análise de comportamento de usuários de planos de telefonia e testes de hipóteses para comparar planos.
        *   `081db06e-c3f8-43e6-91d6-7c1394cf7880 (1).ipynb`: Notebook para análise de planos de telecomunicações.
        *   `sprint4.ipynb`: Notebook adicional para análise de planos de telecomunicações.
        *   `tables`: Subdiretório contendo os datasets utilizados.
    *   **`sprint 6`**: Análise de dados de vendas de videogames. Projeto com foco em limpeza de dados, AED de vendas por plataforma, gênero e região, análise de correlação e testes de hipóteses relacionados a vendas de jogos.
        *   `Analysis.ipynb`: Notebook principal para análise de vendas de videogames.
        *   `Analysis_0.1.ipynb`: Notebook adicional para análise de vendas de videogames.
        *   `data`: Subdiretório contendo os datasets utilizados.
    *   **`Sprint 7`**: Análise de dados de corridas de táxi em Chicago. Foco em AED, visualização de dados e testes de hipóteses relacionados a empresas de táxi e bairros da cidade.
        *   `Analysis_0.1.ipynb`: Notebook principal para análise de dados de táxi.
        *   `data`: Subdiretório contendo os datasets utilizados.
    *   **`sprint 8`**: Análise de métricas de marketing e negócios. Análise de dados de visitas, pedidos e custos para calcular métricas como DAU/WAU/MAU, LTV, CAC e ROI.
        *   `sprint 8.ipynb`: Notebook com a análise de métricas de marketing.
        *   `dados`: Subdiretório contendo os datasets utilizados.
    *   **`Sprint 9`**: Análise de teste A/B. Priorização de hipóteses usando frameworks ICE e RICE, e análise de resultados de um teste A/B para comparar grupos.
        *   `sprint9.ipynb`: Notebook com a análise do teste A/B.
        *   `dados`: Subdiretório contendo os datasets utilizados.
    *   **`sprint 10`**: Análise de dados de restaurantes nos EUA. Foco em análise exploratória de dados de estabelecimentos.
        *   `sprint10.ipynb`: Notebook principal com a análise de dados de restaurantes.
        *   `Análise de Dados de Restaurantes nos EUA.pptx`: Apresentação relacionada à análise.
        *   `px_to_pdf.py`: Script Python para converter notebooks com gráficos Plotly em PDF estático.
        *   `data`: Subdiretório contendo os datasets utilizados.
    *   **`sprint 11`**: Análise de teste A/B sobre o impacto de uma mudança de fonte em um aplicativo móvel. Análise de funil de eventos e testes de proporções (Z-test).
        *   `e3e80813-c474-4f51-b738-53523a6e5fdd.ipynb`: Notebook com revisão do projeto.
        *   `sprint 11.ipynb`: Notebook principal com a análise do teste A/B da fonte.
        *   `data`: Subdiretório contendo os datasets utilizados.
    *   **`Sprint 12`**: Automação de Processamento de Dados. Foco em ETL (Extração, Transformação, Carga) de dados CSV para um banco de dados SQLite usando Python, Pandas e SQLAlchemy.
        *   `Automação`: Subdiretório do projeto de automação.
            *   `Automação.ipynb`: Notebook Jupyter explorando o processo de automação.
            *   `d.py`: (Arquivo vazio conforme input)
            *   `dados`: Subdiretório (potencialmente para dados de entrada/saída).
            *   `database`: Subdiretório para o banco de dados SQLite gerado.

## Executando os Notebooks

Para executar os notebooks Jupyter neste repositório, você precisa ter um ambiente Jupyter configurado. As seguintes opções são recomendadas:

*   **Jupyter Notebook** ou **JupyterLab**: Instalações clássicas do Jupyter, ideais para execução local.
*   **VS Code com Extensão Python**: Editor de código com excelente suporte para notebooks Jupyter.
*   **Google Colab**: Ambiente Jupyter baseado na nuvem, gratuito e acessível via navegador web.

**Passos para executar um notebook:**

1.  **Instalação do Jupyter (se necessário):**
    ```bash
    pip install notebook jupyterlab pandas numpy matplotlib seaborn scipy plotly nbformat nbconvert kaleido sqlalchemy
    ```
    *(Nota: Adicionei as principais bibliotecas usadas nos notebooks à lista de instalação)*
2.  **Navegue até o diretório `Sprints`:** Utilize o terminal ou prompt de comando para acessar o diretório raiz do repositório clonado.
    ```bash
    cd caminho/para/Sprints
    ```
3.  **Inicie o Jupyter:**
    ```bash
    jupyter notebook
    # ou
    jupyter lab
    ```
4.  **Abra o Notebook:** Navegue pela interface Jupyter até o sprint desejado e abra o arquivo `.ipynb`.
5.  **Execute as Células:** Execute o código sequencialmente, célula por célula, usando `Shift + Enter` ou o botão "Run".

Para usuários do Google Colab, é possível fazer upload do diretório `Sprints` para o Google Drive e abrir os notebooks diretamente no Colab. Pode ser necessário instalar bibliotecas adicionais no ambiente Colab (ex: `!pip install ...`).

## Dados

Cada sprint que necessita de dados inclui um subdiretório (`data`, `datasets`, `tables` ou `dados`) para armazenar os arquivos correspondentes. Os notebooks são configurados para ler os dados a partir desses subdiretórios relativos, então certifique-se de manter a estrutura de diretórios ao executar os notebooks localmente ou em outros ambientes.

**Atenção aos Caminhos:** Ao executar os notebooks em um ambiente diferente do original (ex: Colab, outra máquina local), verifique e ajuste os caminhos de leitura dos arquivos (`pd.read_csv()`, etc.) se necessário, para garantir que apontem corretamente para os datasets. Caminhos relativos (ex: `'data/meu_arquivo.csv'`, `'../data/outro_arquivo.csv'`) geralmente funcionarão se a estrutura do diretório for preservada.

Este repositório serve como um portfólio de projetos práticos em análise de dados, demonstrando habilidades em diversas técnicas e ferramentas essenciais para a área.