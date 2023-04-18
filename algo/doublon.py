"""Compte la fréquence de chaque mot et renvoie le premier (et unique) mot 
compté 2 fois"""
def main(card: dict) -> str:
    words = card.get("words")
    word_quantity = {}
    for liste in words:
        for word in liste:
            if not word_quantity.get(word):
                word_quantity[word] = 1
            else: 
                word_quantity[word] += 1
    # renvoie la clé ayant une valeur de 2
    return list(word_quantity.keys())[list(word_quantity.values()).index(2)]

            