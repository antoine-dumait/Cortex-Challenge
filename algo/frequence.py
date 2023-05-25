from collections import Counter
from itertools import chain
def main(card: dict) -> str:
    words = chain(*card.get("words"))
    word_quantity = Counter(words)
    return min(word_quantity, key=word_quantity.get)   