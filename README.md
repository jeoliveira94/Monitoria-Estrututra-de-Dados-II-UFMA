# Monitoria Estrututra de Dados II-UFMA
## Importante
- Deve ser usado o python3 para executar o projeto, leitura do json usando o python3 retorna uma estrutura com objetos strings, já a leitura do json usando o python2 retorna uma estrutura com objetos unicode. 
## Introdução
- Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
- Instruções básicas de como fazer a implementação estão inicio do arquivo /src/algoritmosDeOrdenacao.py

## /src/algoritmosDeOrdenacao.py
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

## Exemplos:
- Modo convencional
  - colecao[i] [operador de comparacao] colecao[j]
  - colecao[i] < colecao[j]

- Modo que você vai usar
  - int(colecao[i]['weight']) [operador de comparacao] int(colecao[j]['weight'])
  - int(colecao[i]['weight']) < int(colecao[j]['weight'])
  - É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
