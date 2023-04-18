"""Compare la couleur du texte au texte en anglais ou en français et renvoie le 
   texte si c'est égale """
def main(card: dict) -> str:
    card_colors = card.get("colors")
    colors_table = {    # dictionnaire français -> anglais
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
}
    
    for (color_text, color_value) in card_colors.items():
        if (color_value == color_text or 
            color_value == colors_table.get(color_text)):
            return color_text