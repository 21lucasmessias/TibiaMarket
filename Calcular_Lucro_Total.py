from Pós_Venda.Todas_Compras import Todas_Compras
from Items_db.Items_Todos import Items_Todos
from Items_db.Items_Green_Djinn import Green_Djinn
from Items_db.Items_Rashid import Rashid
from Items_db.Items_Blue_Djinn import Blue_Djinn


listas = [Rashid]
soma = 0
for lista in listas:
    for itr in lista:
        for item in Todas_Compras:
            if item['name'] == itr['name']:
                lucro = item['quantity'] * (itr['price'] - itr['market'])
                print(f"{item['name']:25} x{item['quantity']:<4} = {lucro}")
                soma += lucro
print(f"\n{'Total':^20} {soma}")
