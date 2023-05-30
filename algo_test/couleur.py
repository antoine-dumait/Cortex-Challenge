def main(card: dict) -> str:
    card_colors = card.get("colors")
    colors_table = {
"argent": "silver", 
"beige": "beige",
"blanc": "white",
"bleu": "blue",
"corail": "coral",
"indigo": "indigo",
"jaune": "yellow",
"lavande": "lavender",
"magenta": "magenta",
"marron": "brown",
"mauve": "purple",
"noir": "black",
"olive": "olive",
"or": "gold",
"orange": "orange",
"orchidée": "orchid",
"rose": "pink",
"rouge": "red",
"saumon": "salmon",
"vert": "green",

"silver": "silver",
"beige": "beige",
"white": "white",
"blue": "blue",
"coral": "coral",
"indigo": "indigo",
"yellow": "yellow",
"lavender": "lavender",
"magenta": "magenta",
"brown": "brown",
"purple": "purple",
"black": "black",
"olive": "olive",
"gold": "gold",
"orange": "orange",
"orchid": "orchid",
"pink": "pink",
"red": "red",
"salmon": "salmon",
"green": "green"
}
    for (color_text, color_value) in card_colors.items():
        if colors_table[color_text] == color_value:
            return color_text