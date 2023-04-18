"Avance un rayon de lumière et change de direction en contact avec un miroir, retourne valeur en fonction de sa position finale"
def main(card: dict) -> int:
    cells = card.get("map") # position en [Y][X]
    lum_pos = [2,4] # position en [x,y] !!
    lum_dir = [0,-1]
    mirrors = {
        "/":-1,
        "\\":1
    }
    while 0 < lum_pos[0] < 5 and 0 < lum_pos[1] < 5:
        if mirrors.get(cells[lum_pos[1]][lum_pos[0]]):
            k=mirrors.get(cells[lum_pos[1]][lum_pos[0]])
            # lors contact miroir la direction (x,y) devient (y,x) * 1 ou -1 en fonction du miroir 
            lum_dir = [lum_dir[1]*k, lum_dir[0]*k] 
        lum_pos = [lum_pos[0] + lum_dir[0],lum_pos[1]+lum_dir[1]]
    # remplacer par dictionnaire plutôt que conditions ?
    if lum_pos[1] == 0: return lum_pos[0] 
    if lum_pos[0] == 5: return lum_pos[1] + 4
    if lum_pos[1] == 5: 
        if lum_pos[0] == 1:
            return 11
        return 13 - lum_pos[0]
    return 16 - lum_pos[1]