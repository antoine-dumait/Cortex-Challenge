def main(card: dict) -> str:
    drawing = card.get("drawing")
    pieces = card.get("pieces")
    index = -1
    rindex = -1
    l = len(drawing)
    for i in range(l):
        if "" in drawing[i]:
            index=i
            break
    for i in range(l):
        if "" in drawing[::-1][i]:
            rindex=l-i
            break
    drawing = [str(row)[1:-1] for row in drawing[index:rindex]]
    for letter,piece in pieces.items():
        if len(drawing) == len(piece):
            for drawing_row, piece_row in zip(drawing, piece):
                if str(["" if c != "" else "X" for c in piece_row])[1:-1] not in drawing_row: 
                    break
            else:
                return letter 