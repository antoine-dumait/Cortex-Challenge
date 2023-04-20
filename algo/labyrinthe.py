"""Traverse le graphe depuis chaque sortie et cherche le départ en utilisant un 
   algorithme DFS (Depth First-Search)"""
def main(card: dict) -> str:
    matrix = card.get("map")
    len_ligne = len(matrix[0])
    len_colonne = len(matrix)
    # correspond aux sorties
    start_pos = [[0,0], [len_ligne-1,0], [len_ligne-1,len_colonne-1], [0,len_colonne-1]]    
    # correspond à gauche, haut, droite, bas
    directions = [[-1,0],[0,-1],[1,0],[0,1]]
    for chiffre, start in enumerate(start_pos):
        stack = [] # vider le stack et visited amélioration de ~ 0.0001 s
        visited = []
        pos = start
        stack.append(start)
        visited.append(start)
        # algo dfs, avance dans les branches du graphes et revient sur ses pas 
        # si départ non trouvé jusqu'à ce que toutes les cases aient été visités
        while stack != []:
            for dir in directions:
                new_pos = [pos[0] + dir[0], pos[1] + dir[1]]
                if (0 <= new_pos[0] < len_ligne and 0 <= new_pos[1] < len_colonne
                and new_pos not in visited and matrix[new_pos[1]][new_pos[0]] != "X"):
                    new_char = matrix[new_pos[1]][new_pos[0]]
                    if new_char == "":
                        pos = new_pos
                        stack.append(pos)
                        visited.append(pos)
                        break
                    elif new_char == "D":
                        pos = new_pos
                        stack.append(pos)
                        visited.append(pos)
                        return chiffre + 1
                    else:
                        pos = new_pos
                        stack.append(pos)
                        visited.append(pos)
            else:
                pos = stack.pop()