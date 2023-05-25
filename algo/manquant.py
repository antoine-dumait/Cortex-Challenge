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
    for liste in (blue,red): # vérifie que les listes avancent de 1 en 1
        liste.sort()
        if len(liste) != liste[-1] - liste[0] + 1:
            x_prev = liste[0]
            for x in liste[1:]:
                if x_prev + 1 != x: return x_prev + 1
                x_prev += 1
