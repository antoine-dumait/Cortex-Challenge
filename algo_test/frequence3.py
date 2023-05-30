from collections import Counter
def main(card: dict) -> str:
    words = card.get("words")
    for i, liste in enumerate(words):
        words[i] = " ".join(liste)
    word_quantity = Counter(words)
    return min(word_quantity, key=word_quantity.get)