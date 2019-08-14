from Log.Log_Formatado import Log_Formatado
from Pós_Venda.Todas_Compras import Todas_Compras

for item_total in Todas_Compras:
    for item_recente in Log_Formatado:
        if item_recente['name'] == item_total['name']:
            item_total['quantity'] += item_recente['quantity']
            break

with open('Todas_Compras.py', 'w') as file:
    file.write(f'Todas_Compras = {Todas_Compras}\n'.replace('}, ', '},\n'))
