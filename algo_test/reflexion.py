"Avance un rayon de lumière et change de direction en contact avec un miroir, retourne valeur en fonction de sa position finale"
def main(card: dict) -> int:
    cells = card.get("map") # position en [Y][X]
    # position en [x,y] !!
    row = 4
    col = 2
    lum_dir = [0,-1]
    mirrors = {
        "/":-1,
        "\\":1
    }
    while 0 < col < 5 and 0 < row < 5:
        mirror=mirrors.get(cells[row][col])
        if mirror: lum_dir = [lum_dir[1]*mirror, lum_dir[0]*mirror] 
        # lors contact miroir la direction (x,y) devient (y,x) * 1 ou -1 en fonction du miroir 
        col += lum_dir[0]
        row  += lum_dir[1]
    # remplacer par dictionnaire plutôt que conditions ?
    if row == 0: return col 
    if col == 5: return row + 4
    if row == 5: 
        if col == 1:
            return 11
        return 13 - col
    return 16 - row