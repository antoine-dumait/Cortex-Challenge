"""Compte la fréquence de chaque mot et renvoie le mot le moins compté"""
def main(card: dict) -> str:
    words = card.get("words")
    word_quantity = {}
    for liste in words:
        for word in liste:
            if not word_quantity.get(word):
                word_quantity[word] = 1
            else: 
                word_quantity[word] += 1
    # retourne la clé la plus petite en prenant comme valeur de comparaison 
    # la valeur de la clé
    return min(word_quantity, key=word_quantity.get)

            