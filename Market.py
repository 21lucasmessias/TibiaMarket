from Personagens.Dans_Girlfriend import Dans_Girlfriend
from Personagens.Rashid_Babrisa import Rashid_Babrisa
from Personagens.Fluffy_Rashid import Fluffy_Rashid
from operator import itemgetter

choice = Fluffy_Rashid
allitems = choice[:]

for e, item in enumerate(choice):
    allitems[e]['quantity'] = allitems[e]['quantity'] // 30
    allitems[e]['lucro'] = allitems[e]['price'] - allitems[e]['market']
    allitems[e]['for10k'] = 10000 / (allitems[e]['price'] - allitems[e]['market'])
    allitems[e]['lucrop'] = ((allitems[e]['price'] - allitems[e]['market']) / allitems[e]['price']) * 100
    allitems[e]['lucro_dia'] = allitems[e]['quantity'] / allitems[e]['for10k'] * 10

sortear_por = 'lucro_dia'
allitems = sorted(allitems, key=itemgetter(sortear_por), reverse=True)

print(f"{'Item':^30}"
      f" {'Preço':>7}"
      f" {'Market':>10}"
      f" {'Lucro/item':>13}"
      f" {'%/item':>9}"
      f" {'Para 10k':>10}"
      f" {'Vendidos/dia':>15}"
      f" {'Lucro/dia':>12}")

for e, i in enumerate(allitems):
    if e == 30:
        break
    if i['quantity'] > 0:
        print(f"{i['name']:^30}"
              f"{i['price']:>8}"
              f"{i['market']:>11}"
              f"{i['lucro']:>14}"
              f"{i['lucrop']:>9.2f}%"
              f"{i['for10k']:>8.0f}"
              f"{i['quantity']:>15}"
              f"{i['lucro_dia']:>13.0f}k")
