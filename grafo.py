import json
import copy
import time

class Grafo(object):
    def __init__(self):
        self.ordenar = None
        self.vertices = None
        self.arestas = None
        return

    def _algortmoDeOrdencaoErro(self):
        if self.ordenar is None: 
            print('Algoritmo de Ordencação Nulo, finalizando programa.')
            raise ValueError

    def setAlgoritmoDeOrdencao(self, algoritimoDeOrdenacao):
        self.ordenar = algoritimoDeOrdenacao

    def executarKruskal(self):
        self._algortmoDeOrdencaoErro()
        return self._kruskal()

    def _conectaDuasArvoresDiferentes(self, floresta, aresta):
        for arvore in floresta:
            if aresta['source'] in arvore and aresta['target'] in arvore:
                return False
        return True

    def _concatenaArvores(self, floresta, aresta):
        arvoreA = None
        arvoreB = None
        for arvore in floresta:
            if(aresta['source'] in arvore):
                arvoreA = arvore
            if(aresta['target'] in arvore):
                arvoreB = arvore     
        if arvoreA is not None and arvoreB is not None:
            if arvoreA != arvoreB:
                novaArvore = arvoreA + arvoreB
                floresta.remove(arvoreA)
                floresta.remove(arvoreB)
                floresta.append(novaArvore)

    def _kruskal(self):
        print('Executando kruskal, aguarde...')
        print('Ordenando arestas')
        self._algortmoDeOrdencaoErro()
        floresta =  [ [vertice['id'] ] for vertice in self.vertices]
        arvoreGeradoraMinima = []
        inicio = time.time()
        arestas = self.ordenar(copy.copy(self.arestas))
        fim = time.time()
        print("Tempo de execução do algoritmo de ordenação : " ,fim - inicio)

        while len(arestas):
            aresta = arestas.pop(0)
            if(self._conectaDuasArvoresDiferentes(floresta, aresta)):
                arvoreGeradoraMinima.append(aresta)
                self._concatenaArvores(floresta, aresta)
        return arvoreGeradoraMinima

    def carregarGrafo(self, arquivoJson):
        print('Carregando grafo, aguarde...')
        with open(arquivoJson) as arquivo:
            grafo_json = json.loads(arquivo.read())
            self.vertices = grafo_json['graph']['nodes']
            self.arestas = grafo_json['graph']['edges']
        return True    