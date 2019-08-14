from Log.Log_Formatado import Log_Formatado
from Items_db.Items_Todos import Items_Todos
from Items_db.Items_Green_Djinn import Green_Djinn
from Items_db.Items_Rashid import Rashid
from Items_db.Items_Blue_Djinn import Blue_Djinn

soma = 0
listas = [Green_Djinn]

for lista in listas:
    for item in Log_Formatado:
        for it in lista:
            if item['name'] == it['name']:
                lucro = item['quantity'] * (it['price'] - it['market'])
                print(f"{item['name']:25} x{item['quantity']:4} {lucro:8} ")
                soma += lucro
print(f"\n{'Total':^25} {soma}")
