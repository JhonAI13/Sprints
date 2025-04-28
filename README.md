# Repositório Sprints - Projetos de Análise de Dados

Este repositório contém uma coleção de Jupyter Notebooks (`.ipynb`) e arquivos de dados correspondentes, organizados em sprints de análise de dados. Cada sprint é dedicado a um projeto específico, abrangendo diversas etapas do processo de análise, desde a limpeza e preparação dos dados até a análise exploratória (AED) e testes de hipóteses estatísticas.

## Estrutura do Repositório

O repositório está organizado nos seguintes diretórios:

*   **`Sprints`**: Diretório raiz contendo este arquivo `README.md` e subdiretórios para cada sprint.
    *   **`sprint 1`**: Avaliação e preparação de dados de clientes de e-commerce. Sprint introdutório com foco em qualidade e limpeza de dados.
        *   `sprint 1.ipynb`: Notebook focado na limpeza e preparação de dados de e-commerce.
    *   **`sprint 2`**: Análise de dados de um serviço de streaming de música. Projeto sobre pré-processamento de dados musicais e teste de hipóteses sobre preferências musicais entre cidades.
        *   `20c53b4a-81d8-4d18-bc38-d36d30ae6fba (1).ipynb`: Notebook para análise do serviço de música.
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
## Executando os Notebooks

Para executar os notebooks Jupyter neste repositório, você precisa ter um ambiente Jupyter configurado. As seguintes opções são recomendadas:

*   **Jupyter Notebook** ou **JupyterLab**: Instalações clássicas do Jupyter, ideais para execução local.
*   **VS Code com Extensão Python**: Editor de código com excelente suporte para notebooks Jupyter.
*   **Google Colab**: Ambiente Jupyter baseado na nuvem, gratuito e acessível via navegador web.

**Passos para executar um notebook:**

1.  **Instalação do Jupyter (se necessário):**
    ```bash
    pip install notebook jupyterlab
    ```
2.  **Navegue até o diretório `Sprints`:** Utilize o terminal ou prompt de comando para acessar o diretório raiz do repositório.
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

Para usuários do Google Colab, é possível fazer upload do diretório `Sprints` para o Google Drive e abrir os notebooks diretamente no Colab.

## Dados

Cada sprint que necessita de dados inclui um subdiretório `data`, `datasets` ou `tables` para armazenar os arquivos. Os notebooks são configurados para ler os dados a partir desses subdiretórios, então certifique-se de manter a estrutura de diretórios ao executar os notebooks localmente ou no Colab.

**Atenção aos Caminhos:** Ao executar os notebooks em um ambiente diferente, verifique e ajuste os caminhos de arquivos se necessário para garantir que apontem corretamente para os datasets. Caminhos relativos (ex: `'data\\meu_arquivo.csv'`) geralmente funcionarão se a estrutura do diretório for preservada.

Este repositório serve como um portfólio de projetos práticos em análise de dados, demonstrando habilidades em diversas técnicas e ferramentas essenciais para a área.