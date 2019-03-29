def SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima):
    with open(arquivoDeSaida, 'w') as arquivo:
        for aresta in arvoreGeradoraMinima:
            arquivo.write('fonte: {}, destino: {}, peso: {}\n'.format(aresta['source'], aresta['target'], aresta['weight']))
