"""Permet de choisir quelle carte tester en utilisant la fonction jouer de joueur"""
import joueurs.binome4 as joueur
import json
import os
import time
# numéro des cartes en fonction du problème
# couleur 1, 10
# relfexion 2, 11
# calcul 3, 12
# fréquence 4, 9
# manquant 5, 13
# labyrinthe 6, 14
# doublon 7, 15
# raisonnement 8, 16
card_number = 14
# construit chemin absolu de la carte
dir_path = os.path.dirname(__file__) 
file_path = f"cards/card-{card_number}.json"
abs_path = os.path.join(dir_path,file_path)
with open(abs_path, 'r', encoding='utf-8') as card: # utilise utf-8 pour avoir les accents
    card = json.load(card)
    start_time = time.perf_counter()
    resultat = joueur.jouer(card)
    print(resultat)
    print("--- %s seconds ---" % (time.perf_counter() - start_time))