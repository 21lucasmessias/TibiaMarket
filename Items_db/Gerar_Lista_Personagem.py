from Items_db.Items_Blue_Djinn import Blue_Djinn
from Items_db.Items_Rashid import Rashid
from Items_db.Items_Green_Djinn import Green_Djinn
from operator import itemgetter

# list_items = Colocar os nomes das listas (from rashid import rashid_list)
list_items = [Green_Djinn]

# guarda o dicionario daquele item
item_dict = {}

# armazena o dicionario do item na lista
item_list_dict = list()

# faz a magica
for lista in list_items:
    for item in lista:
        item_dict['name'] = item['name']
        item_dict['price'] = item['price']
        item_dict['quantity'] = item['quantity']
        item_dict['market'] = item['market']
        item_list_dict.append(item_dict.copy())
        item_dict.clear()

# com itemgetter podemos dar sort nos dicionarios
item_list_dict = sorted(item_list_dict, key=itemgetter('name'))

# output da nova lista no arquivo
destino = 'C:\\Users\\Kash\Documents\\Arquivos\\Python\\Tibia_Market\\Personagens\\Fluffy_Rashid.py'
with open(destino, 'w') as file:
    file.write(f'Fluffy_Rashid = {item_list_dict}\n'.replace('}, ', '},\n'))
