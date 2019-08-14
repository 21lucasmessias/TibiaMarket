from operator import itemgetter

item = {}
item_lista = list()

with open('Log.txt', 'r') as file:
    while True:
        linha = file.readline()
        if linha == '':
            break
        condicao = False
        nome = str(linha[linha.find('x') + 2:linha.find(' for')]).replace("'", '').title()
        linha = linha.split()
        item['name'] = nome
        item['quantity'] = int(linha[2].replace('x', ''))
        for i in item_lista:
            if item['name'] == i['name']:
                i['quantity'] += item['quantity']
                item.clear()
                condicao = True
                break
        if not condicao:
            item_lista.append(item.copy())
            item.clear()

item_lista = sorted(item_lista, key=itemgetter('name'))

with open('Log_Formatado.py', 'w') as lf:
    lf.write(f'Log_Formatado = {item_lista}\n'.replace('}, ', '},\n'))
