from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão inicia do arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":

    algoritimoDeOrdenacao = insertionSort
    arquivoJson = '7vertices.json'
    arquivoDeSaida = 'mst7Vertices.txt'

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    escrever(arquivoDeSaida, arvoreGeradoraMinima)

