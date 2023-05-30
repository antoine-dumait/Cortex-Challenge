"""Compte la fréquence de chaque mot et renvoie le premier (et unique) mot 
compté 2 fois"""
from itertools import chain
def main(card: dict) -> str:
    words = list(chain(*card.get("words")))
    all_word = set(words)
    words = "".join(words)
    for word in all_word:
        if words.count(word) == 2:
            return word