from collections import Counter
from itertools import chain
def main(card: dict) -> str:
    words = chain(*card.get("words"))
    words_quantity = Counter(words)
    return list(words_quantity.keys())[list(words_quantity.values()).index(2)]