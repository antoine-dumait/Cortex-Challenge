def main(card: dict) -> int:
    cells = card.get("map")
    row = 4
    col = 2
    lum_dir = [0,-1]
    while 0 < col < 5 and 0 < row < 5:
        cell = cells[row][col]
        if cell != "":
            if cell == "/": mirror = -1
            else: mirror = 1
            lum_dir = [lum_dir[1]*mirror, lum_dir[0]*mirror] 
        col += lum_dir[0]
        row  += lum_dir[1]
    if row == 0: return col 
    if col == 5: return row + 4
    if row == 5: 
        if col == 1:
            return 11
        return 13 - col
    return 16 - row