from collections import Counter
from itertools import chain
def main(card: dict) -> str:
    words = chain(*card.get("words"))
    words_quantity = Counter(words)
    for key,value in words_quantity.items():
        if value == 2:
            return key