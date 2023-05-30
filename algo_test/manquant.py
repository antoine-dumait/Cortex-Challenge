"""Vérifie que la suite bleu puis rouge sont des suites numériques 
sinon renvoie le nombre manquant"""
def main(card: dict) -> str:
    numbers = card.get("numbers")
    red = []
    blue = []
    for s in numbers: # ajoute les nombres à leur liste 
        if "R" == s[-1]:
            red.append(int(s[:-1]))
        else: 
            blue.append(int(s[:-1]))
    total = sum(red)
    normal = sum(range(min(red), max(red)+1))
    if total != normal:
        return normal - total
    else:
        return sum(range(min(blue), max(blue)+1)) - sum(blue)