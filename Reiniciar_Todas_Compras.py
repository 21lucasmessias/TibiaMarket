from Items_db.Items_Todos import Items_Todos

Todas_Compras = []
novoitem = {}

for item in Items_Todos:
    novoitem = {'name': item['name'], 'quantity':0}
    Todas_Compras.append(novoitem)

with open('Todas_Compras.py', 'w') as file:
    file.write(f'Todas_Compras = {Todas_Compras}\n'.replace('}, ', '},\n'))
