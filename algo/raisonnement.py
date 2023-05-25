def main(card :dict):

    drawing=card.get("drawing")
    pieces=card.get("pieces")
    min_x = -1
    min_y = -1
    for i in range(len(drawing)):
        try:
            if min_x == -1: 
                min_x = drawing[i].index("")
            else:
                min_x = min(min_x,drawing[i].index(""))
            if min_y == -1:
                min_y = i
        except:
            pass
    for letter,piece in pieces.items():
        width_piece = len(piece[0])
        for row_piece, row_drawing in zip(piece, drawing[min_y:]):
            if ["X" if c != "X" else "" for c in row_piece] != row_drawing[min_x:min_x+width_piece]:
                break
        else:
            return letter