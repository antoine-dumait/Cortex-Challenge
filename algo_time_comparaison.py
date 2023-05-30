'''Ce programme permet de tester autant d'algo voulu en utilisant des données
aléatoire créer par create_card.py. Il vous suffit d'importer un algo pour le tester
en le nommant avec la bonne convention. (2 + x pour les algos de test)
'''
import json
import time

import algo.couleur as couleur
import algo.reflexion as reflexion
import algo.frequence as frequence
import algo.manquant as manquant
import algo.doublon as doublon
import algo.raisonnement as raisonnement
import algo.calcul as calcul
import algo.labyrinthe as labyrinthe

import algo_test.couleur as couleur2
import algo_test.reflexion as reflexion2
import algo_test.frequence as frequence2 
import algo_test.manquant as manquant2
import algo_test.doublon2 as doublon2
import algo_test.doublon as doublon3
import algo_test.raisonnement as raisonnement2
import algo_test.calcul2 as calcul2
import algo_test.labyrinthe as labyrinthe2

import create_card as create
# numéro des cartes en fonction du problème
# couleur 1, 10
# reflexion 2, 11
# calcul 3, 12
# fréquence 4, 9
# manquant 5, 13
# labyrinthe 6, 14
# doublon 7, 15
# raisonnement 8, 16
dict_card_num = {
    "labyrinthe": (6,14),
    "raisonnement": (8, 16)
}

fonc_dict = {1:"couleur",
            2:"reflexion", 
            3:"calcul",
            4:"frequence",
            5:"manquant",
            6:"labyrinthe",
            7:"doublon",
            8:"raisonnement"}

number_fonc = 1 #numéro de la fonction
number_of_cards = 1000 #nombres de cartes
number_of_try = 1000 #nombres d'itération pour chaque carte


fonc_name = fonc_dict[number_fonc]
fonc_x = 1
fonctions = []
while globals().get(fonc_name): #permet de tester toutes les fonctions importés
    print(fonc_name)
    fonctions.append(globals()[fonc_name])
    fonc_x+=1
    if fonc_x > 2:
        fonc_name = fonc_name[:-1] + str(fonc_x)
    else:
        fonc_name = fonc_name + "2"
fonc_name = fonc_dict[number_fonc]
times = [0] * len(fonctions)
card_func = [8]
#fût utile quand tout les algos de création de cartes n'étaient pas encore disponible
if number_fonc in card_func: 
    number_of_cards = len(dict_card_num[fonc_name])
for i in range(number_of_cards):
    #choisis carte en fonction disponibilité des algos création
    if number_fonc not in card_func:
        data = create.get(fonc_name)
        card = data[0]
        result_card = data[1]
        type = card.get("type", None)
    else:
        file_path = f"cards/card-{dict_card_num[fonc_name][i]}.json"
        with open(file_path, 'r', encoding='utf-8') as card:
            card = json.load(card)
            type = card.get("type", None)
            result_card = False
    for i,fonc in enumerate(fonctions):
        for j in range(number_of_try):
            start_time = time.perf_counter()
            result = fonc.main(card)
            times[i] += time.perf_counter() - start_time
            if fonc.__name__.find("calcul") > -1:
                if sum([int(i) for i in result.split("+")]) != sum([int(i) for i in result_card.split("+")]):
                    print(f'{result=}')
                    print(f'{result_card=}')
                    print(f'{fonc.__name__=}')
                    print(card)
                    break
            elif result_card and result != result_card:
                print(f'{result=}')
                print(f'{result_card=}')
                print(f'{fonc.__name__=}')
                print(card)
                break
        else:
            continue
        break
    else:
        continue
    break
#calcul moyenne des algos
for i in range(len(times)):
    times[i] = times[i]/number_of_cards/number_of_try 
for i,(f,t) in enumerate(zip([f.__name__ for f in fonctions], times)):
    print(f'{f:25} {i+1:5} --- {t:.10f} seconds ---')