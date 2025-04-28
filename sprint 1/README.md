# Sprint 1: Avaliação e Preparação de Dados de Clientes

## Qual o objetivo do sprint?

Neste primeiro sprint, minha tarefa foi dar uma olhada inicial nos dados coletados pela empresa de e-commerce Store 1. O objetivo principal era **avaliar a qualidade** dessa amostra de dados de clientes e **prepará-la** para análises futuras. Isso envolveu identificar e corrigir problemas comuns em dados brutos, como:

*   Tipos de dados inadequados (por exemplo, idade como float em vez de int).
*   Formatação inconsistente em strings (espaços extras, uso de underscores, letras maiúsculas/minúsculas).
*   Possíveis erros em valores que poderiam quebrar o código (como tentar converter texto em número).
*   Estruturar os dados de forma mais útil (como separar nome e sobrenome).

Basicamente, foi um sprint focado em **limpeza e organização inicial** dos dados, garantindo que eles estivessem consistentes e prontos para serem usados.

## Quais tecnologias usei?

Para realizar essa avaliação e preparação, utilizei principalmente **Python puro**. As funcionalidades e técnicas específicas incluíram:

*   **Manipulação de Strings:** Métodos como `.strip()`, `.replace()`, `.split()` e `.lower()` para limpar e padronizar nomes e categorias.
*   **Conversão de Tipos:** Uso de `int()` para corrigir o tipo da coluna de idade.
*   **Estruturas de Controle:** Loops `for` para iterar sobre listas (como categorias favoritas e a tabela de usuários) e `while` para simular compras até atingir um valor.
*   **Tratamento de Erros:** Blocos `try-except` para lidar com potenciais erros durante a conversão de tipos de dados (idade).
*   **Estruturas de Dados:** Trabalho com variáveis básicas, listas e listas aninhadas (para simular a estrutura de uma tabela).
*   **Funções Embutidas:** Uso de `sum()`, `max()`, `min()` para cálculos básicos de gastos.
*   **Módulo `random`:** Especificamente `randint` para simular valores de novas compras.
*   **Formatação de Strings:** F-strings para criar strings resumidas com informações do usuário.

*Observação: Neste sprint específico, não utilizei bibliotecas de análise de dados como Pandas ou NumPy, focando nas ferramentas básicas do Python para manipulação de dados.*

## Quais competências eu consegui?

Ao completar este sprint, demonstrei e reforcei competências em:

*   **Avaliação da Qualidade de Dados:** Consegui identificar inconsistências e problemas em dados brutos (tipos, formatos, valores inesperados).
*   **Limpeza e Pré-processamento de Dados:** Apliquei técnicas para corrigir os problemas identificados, como normalização de strings e conversão de tipos.
*   **Programação Básica em Python:** Utilizei laços de repetição (`for`, `while`), condicionais (`if`), tratamento de exceções (`try-except`) e manipulação de listas e strings de forma eficaz.
*   **Lógica de Programação:** Implementei algoritmos simples para calcular totais, encontrar mínimos/máximos, filtrar dados com base em condições e simular processos (como atingir um valor alvo de compras).
*   **Atenção aos Detalhes:** Percebi problemas sutis como espaços extras e a necessidade de padronização de caixa (maiúsculas/minúsculas).
*   **Resolução de Problemas:** Encontrei e implementei soluções para cada um dos problemas de dados apresentados nas tarefas.
