def escrever(out, obj):
    with open(out, 'w') as arq:
        for item in obj:
            arq.write('fonte: {}, destino: {}, peso: {}\n'.format(item['source'], item['target'], item['weight']))
