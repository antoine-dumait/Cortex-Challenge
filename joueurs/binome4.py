"""
L1 - MI-I : Concrétisation disciplinaire -- Cortex Challenge
"""

__team__ = "Binôme 4"
__authors__ = ["Antoine DUMAIT", "Islem HOCINI"]
__date__ = "18/04/2023"
__version__ = "0.1"

from typing import Union
import algo.couleur as couleur
import algo.reflexion as reflexion
import algo.frequence as frequence
import algo.manquant as manquant
import algo.doublon as doublon
import algo.raisonnement as raisonnement
import algo.calcul as calcul

def jouer(card: dict) -> Union[None, str, int]:
    '''
    Fonction commune à tous les groupes permettant de jouer tous ensemble
    :param card: la carte au format JSON
    :return: le résultat trouvé par son joueur. Si type non implémenté return None.
    '''
    type = card.get("type", None)
   
    if type == "couleur": return couleur.main(card)
    if type == "réflexion": return reflexion.main(card)
    if type == "fréquence": return frequence.main(card)
    if type == "manquant": return manquant.main(card)
    if type == "doublon": return doublon.main(card)
    if type == "raisonnement": return raisonnement.main(card)
    if type == "calcul": return calcul.main(card)
    
    return None
