"""Compare la pièce manquante aux pièces disponibles et 
   renvoie la pièce correspondante"""
def main(card: dict) -> str:
    drawing = card.get("drawing")
    pieces = card.get("pieces")
    len_drawing = len(drawing[0])
    first, last = len_drawing, 0
    start, end = 0, len(drawing)
    # récupere la position du coté haut gauche (first) et du coté bas droite (last)
    # ainsi que les lignes dans laquelle la pièce manquante n'est pas incluse (start, end)
    for ligne in drawing: 
        try:              
            first = min(first, ligne.index(""))
            last = max(last, len_drawing - ligne[::-1].index(""))
        except:
            # first != 0 quand premiere symbole trouvé
            if first == len_drawing: start+=1 
            else: end -= 1
    hole_value = [ligne[first:last] for ligne in drawing[start:end]] #correspond à la pièce manquante
    len_hole = len(hole_value)
    for letter,piece in pieces.items():
        if len(piece) == len_hole and len(piece[0]) == len(hole_value[0]):
            for ligne_p,ligne_h in zip(piece, hole_value):
                for case_p,case_h in zip(ligne_p, ligne_h):
                    # pièce manquante est composé de "" tandis que les pièces disponibles 
                    # sont composés de "X", si égale pas la bonne pièce
                    if case_p == case_h: 
                        break            
                else: # permet de sauter le break si il n'y pas eu de break dans la boucle, 
                      # sinon sort de la boucle supérieur aussi
                    continue
                break  
            else: # return letter seulement si la boucle inférieur n'a pas break
                return letter