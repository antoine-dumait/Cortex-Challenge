"""Permet de choisir quelle carte tester en utilisant la fonction jouer de joueur"""
import joueurs.binome4 as joueur
import json
import os
# numéro des cartes en fonction du problème
# couleur 1, 10
# relfexion 2, 11
# fréquence 4, 9
# manquant 5, 13
# doublon 7, 15
# raisonnement 8, 16
# calcul 3, 12
# labyrinthe 6, 14
card_number = 12
# construit chemin absolu de la carte
dir_path = os.path.dirname(__file__) 
file_path = f"cards/card-{card_number}.json"
abs_path = os.path.join(dir_path,file_path)
with open(abs_path, 'r', encoding='utf-8') as card: # utilise utf-8 pour avoir les accents
    card = json.load(card)
    print(joueur.jouer(card))