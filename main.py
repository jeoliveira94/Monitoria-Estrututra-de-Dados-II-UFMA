from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

#comparacoes
#print(int(arestas[0]['weight']) > int(arestas[1]['weight']))
#print(int(arestas[0]['weight']) < int(arestas[1]['weight']))
#print(int(arestas[0]['weight']) == int(arestas[1]['weight']))

if __name__ == "__main__":
    
    algoritimoDeOrdenacao = selecionSort
    #algoritimoDeOrdenacao = insertionSort
    
    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo('7vertices.json')
    mst100 =  grafo.executarKruskal() 
    escrever('mst100.txt', mst100)

