Tibia Market

Qualquer problema me enviar um email : 21.lucasmessias@gmail.com

O usuario deve informar um dictionary que contenha os itens que lhe interessam e importar no Market.py

Exemplo do dictionary:

Fluffy_Rashid = [{'name': 'Bonebreaker', 'price': 10000, 'quantity': 15, 'market': 8500},
                 {'name': 'Dragon Hammer', 'price': 2000, 'quantity': 130, 'market': 1000},
                 {'name': 'Dreaded Cleaver', 'price': 15000, 'quantity': 30, 'market': 12000},
                 {'name': 'Giant Sword', 'price': 17000, 'quantity': 30, 'market': 11000},
                 {'name': 'Hailstorm Rod', 'price': 3000, 'quantity': 100, 'market': 2025},
                 {'name': 'Haunted Blade', 'price': 8000, 'quantity': 140, 'market': 6000},
                 {'name': 'Knight Armor', 'price': 5000, 'quantity': 355, 'market': 3800},
                 {'name': 'Knight Axe', 'price': 2000, 'quantity': 130, 'market': 1155},
                 {'name': 'Knight Legs', 'price': 5000, 'quantity': 500, 'market': 4050},
                 {'name': 'Necrotic Rod', 'price': 1000, 'quantity': 120, 'market': 500},
                 {'name': 'Northwind Rod', 'price': 1500, 'quantity': 55, 'market': 700},
                 {'name': 'Onyx Flail', 'price': 22000, 'quantity': 10, 'market': 11000},
                 {'name': 'Serpent Sword', 'price': 900, 'quantity': 80, 'market': 300},
                 {'name': 'Skull Staff', 'price': 6000, 'quantity': 100, 'market': 4000},
                 {'name': 'Springsprout Rod', 'price': 3600, 'quantity': 90, 'market': 2720},
                 {'name': 'Terra Rod', 'price': 2000, 'quantity': 270, 'market': 1000},
                 {'name': 'Titan Axe', 'price': 4000, 'quantity': 70, 'market': 2000},
                 {'name': 'Tower Shield', 'price': 8000, 'quantity': 220, 'market': 6000},
                 {'name': 'Underworld Rod', 'price': 4400, 'quantity': 200, 'market': 3100},
                 {'name': 'Vampire Shield', 'price': 15000, 'quantity': 75, 'market': 12000},
                 {'name': 'Warrior Helmet', 'price': 5000, 'quantity': 250, 'market': 4070}]
                 
                 
E entao executar o arquivo Market.py


Utilizando o dict acima, obtemos : 
             Item                Preço     Market    Lucro/item    %/item   Para 10k    Vendidos/dia    Lucro/dia
         Knight Legs              5000       4050           950    19.00%      11             16           15k
         Tower Shield             8000       6000          2000    25.00%       5              7           14k
         Knight Armor             5000       3800          1200    24.00%       8             11           13k
          Terra Rod               2000       1000          1000    50.00%      10              9            9k
        Haunted Blade             8000       6000          2000    25.00%       5              4            8k
        Underworld Rod            4400       3100          1300    29.55%       8              6            8k
        Warrior Helmet            5000       4070           930    18.60%      11              8            7k
         Giant Sword             17000      11000          6000    35.29%       2              1            6k
         Skull Staff              6000       4000          2000    33.33%       5              3            6k
        Vampire Shield           15000      12000          3000    20.00%       3              2            6k
        Dragon Hammer             2000       1000          1000    50.00%      10              4            4k
          Titan Axe               4000       2000          2000    50.00%       5              2            4k
          Knight Axe              2000       1155           845    42.25%      12              4            3k
       Dreaded Cleaver           15000      12000          3000    20.00%       3              1            3k
        Hailstorm Rod             3000       2025           975    32.50%      10              3            3k
       Springsprout Rod           3600       2720           880    24.44%      11              3            3k
         Necrotic Rod             1000        500           500    50.00%      20              4            2k
        Serpent Sword              900        300           600    66.67%      17              2            1k
        Northwind Rod             1500        700           800    53.33%      12              1            1k



A pasta /Log , contem um utilitario para que voce organize suas ultimas vendas, inserindo o texto que é gerado na janela do proprio jogo apos a venda, ele ira formatar diretamente para um dict, que sera utilizado nos algoritmos de lucro

Exemplo de Log.txt:

12:51 Sold 20x knight legs for 100000 gold.
12:52 Sold 34x underworld rod for 149600 gold.
12:52 Sold 13x springsprout rod for 46800 gold.
12:54 Sold 10x warrior helmet for 50000 gold.
12:54 Sold 4x haunted blade for 32000 gold.
12:54 Sold 4x titan axe for 16000 gold.
12:54 Sold 1x knight legs for 5000 gold.
12:54 Sold 1x skull staff for 6000 gold.
12:54 Sold 15x tower shield for 120000 gold.
12:54 Sold 7x knight armor for 35000 gold.
12:54 Sold 7x knight armor for 35000 gold.
12:54 Sold 3x knight armor for 15000 gold.
12:54 Sold 8x tower shield for 64000 gold.
12:54 Sold 18x knight legs for 90000 gold.
12:55 Sold 4x dragon hammer for 8000 gold.
12:55 Sold 4x knight axe for 8000 gold.
12:55 Sold 4x skull staff for 24000 gold.
12:55 Sold 1x dreaded cleaver for 15000 gold.
12:55 Sold 1x giant sword for 17000 gold.
12:55 Sold 1x knight armor for 5000 gold.
12:55 Sold 1x knight legs for 5000 gold.

Saida do Gerar_Log.py em formato de dict em Log_Formatado.py:

Log_Formatado = [{'name': 'Dragon Hammer', 'quantity': 4},
{'name': 'Dreaded Cleaver', 'quantity': 1},
{'name': 'Giant Sword', 'quantity': 1},
{'name': 'Haunted Blade', 'quantity': 4},
{'name': 'Knight Armor', 'quantity': 18},
{'name': 'Knight Axe', 'quantity': 4},
{'name': 'Knight Legs', 'quantity': 40},
{'name': 'Skull Staff', 'quantity': 5},
{'name': 'Springsprout Rod', 'quantity': 13},
{'name': 'Titan Axe', 'quantity': 4},
{'name': 'Tower Shield', 'quantity': 23},
{'name': 'Underworld Rod', 'quantity': 34},
{'name': 'Warrior Helmet', 'quantity': 10}]

Utilizando entao o algoritmo Adicionar_Compra.py , podemos introduzir essas novas vendas ao banco de dados, que é salvo em Todas_Compras.py, e podemos calcular o lucro recente com Calcular_Lucro_Recente.py, ou calcular o lucro total desde que comecou a utilizar o programa Calcular_Lucro_Total.py 
