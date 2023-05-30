from collections import Counter
from itertools import chain
def main(card: dict) -> str:
    words = card.get("words")
    s = " ".join(" ".join(liste) for liste in words)
    word_quantity = {i:s.count(i) for i in set(chain(*words))}
    return min(word_quantity, key=word_quantity.get)