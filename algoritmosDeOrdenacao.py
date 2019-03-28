#comparacoes
#print(int(arestas[0]['weight']) > int(arestas[1]['weight']))
#print(int(arestas[0]['weight']) < int(arestas[1]['weight']))
#print(int(arestas[0]['weight']) == int(arestas[1]['weight']))

def insertionSort(colecao):
    for i in range(1, len(colecao)): 
        key = colecao[i] 
        j = i-1
        while j >= 0 and key['weight'] < colecao[j]['weight']: 
            colecao[j + 1] = colecao[j] 
            j -= 1
        colecao[j + 1] = key
    return

def selecionSort(colecao): 
    for i in range(len(colecao)): 
        min_idx = i 
        for j in range(i+1, len(colecao)): 
            if int(colecao[min_idx]['weight']) > int(colecao[j]['weight']): 
                min_idx = j
        colecao[i], colecao[min_idx] = colecao[min_idx], colecao[i] 
    return colecao