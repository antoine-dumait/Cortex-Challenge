def main(card: dict) -> str:
    numbers = card.get("numbers")
    red = []
    blue = []
    for s in numbers:
        if "R" == s[-1]:
            red.append(int(s[:-1]))
        else: 
            blue.append(int(s[:-1]))
    for liste in (blue,red):
        liste.sort()
        if len(liste) != liste[-1] - liste[0] + 1:
            x_prev = liste[0]
            for x in liste[1:]:
                if x_prev + 1 != x: return x_prev + 1
                x_prev += 1
