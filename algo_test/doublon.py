def main(card: dict) -> str:
    words = card.get("words")
    in1 = set()
    in2 = set()
    non = set()
    for liste in words:
        for mot in liste:
            if mot not in non:
                if mot in in1 :
                    in1.remove(mot)
                    in2.add(mot)
                elif mot in in2:
                    in2.remove(mot)
                    non.add(mot)
                else:
                    in1.add(mot)
    return next(iter(in2))