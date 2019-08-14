from Todas_Compras import Todas_Compras

for item in Todas_Compras:
    item['quantity'] = 0

with open('Todas_Compras.py', 'w') as file:
    file.write(f'Todas_Compras = {Todas_Compras}\n'.replace('}, ', '},\n'))
