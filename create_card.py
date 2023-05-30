from random import randint,shuffle


def frequence(taille=None, nombre_mots=None) -> list[list]:
    if taille == None: taille = randint(1,100)
    if nombre_mots == None: nombre_mots = randint(1,100)
    size_file = 100
    nombre_mots = min(size_file, nombre_mots, taille*2//2)
    with open("words.txt") as file_words:
        words = file_words.read().split()
    if nombre_mots < size_file:
        deleted = 0
        for i in range(size_file-nombre_mots):
            words.pop(randint(0,size_file-1-deleted))
            deleted += 1
    matrix = []
    quantity = [0]*nombre_mots
    for n in range(taille):
        ligne = []
        for i in range(taille):
            r = randint(0,nombre_mots-1)
            quantity[r] += 1
            ligne.append(words[r])
        matrix.append(ligne)
    mini = min(i for i in quantity if i > 0)
    if mini > 1:
        result = words[quantity.index(mini)]
        result2 = words[nombre_mots - 1 - quantity[::-1].index(mini)]
        if result != result2:
            for y in range(taille):
                if matrix[y].count(result) > 0:
                    ind = matrix[y].index(result)
                    matrix[y][ind] = result2
                    break
    else:
        result = words[quantity.index(mini)]
        result2 = words[::-1][quantity[::-1].index(mini)]
        while result != result2:
            r = [randint(0, taille -1), randint(0, taille -1)]
            while quantity[words.index(matrix[r[0]][r[1]])] < mini + 2:
                r = [(r[0]+1)%taille, (r[1] + (1 if r[0] == taille -1 else 0))%taille]
            quantity[words.index(matrix[r[0]][r[1]])] -= 1
            quantity[words.index(result2)] += 1
            matrix[r[0]][r[1]] = result2
            result2 = words[::-1][quantity[::-1].index(mini)]
    return matrix, result


def doublon(taille=None, nombre_mots=None) -> list[list]:
    if taille == None: taille = randint(1,100)
    if nombre_mots == None: nombre_mots = randint(1,100)
    size_file = 100
    nombre_mots = max(2,min(size_file, nombre_mots))
    taille = max(2, taille)
    with open("words.txt") as file_words:
        words = file_words.read().split()
    if nombre_mots < size_file:
        deleted = 0
        for i in range(size_file-nombre_mots):
            words.pop(randint(0,size_file-1-deleted))
            deleted += 1
    result = words.pop(randint(0,nombre_mots-1))
    nombre_mots -= 1
    matrix = []
    quantity = [0]*nombre_mots
    r1 = (randint(0, taille-1), randint(0, taille-1))
    r2 = r1
    while r2 == r1:
        r2 = (randint(0, taille-1), randint(0, taille-1))
    for x in range(taille):
        ligne = []
        for y in range(taille):
            if (x,y) in [r1,r2]:
                ligne.append(result)
            else:
                r = randint(0,nombre_mots-1)
                quantity[r] += 1
                ligne.append(words[r])
                if quantity[r] == 2:
                    quantity[r] += 1
                    ligne.append(words[r])
        matrix.append(ligne)
    return matrix, result


def couleur(taille=None):
    if taille == None: taille = randint(1,20)
    taille = min(20, taille)
    colors = {}
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
    len_colors = len(colors_table)
    for i in range(taille):
        color_text = None
        while not color_text or color_text in colors.keys():
            color_text = list(colors_table.keys())[randint(0, len_colors-1)] if randint(0,1) else list(colors_table.values())[randint(0, len_colors-1)]
        color_value = None
        while not color_value or color_value == color_text or color_value == colors_table.get(color_text):
            color_value = list(colors_table.values())[randint(0, len_colors-1)]
        colors[color_text] = color_value
    r = randint(0, taille-1)
    result = list(colors.keys())[r]
    colors[result] = colors_table[result] if result in colors_table.keys() else result
    return colors, result


def reflexion(mirror_count = None):
    if mirror_count == None: mirror_count = randint(1,16)
    mirror_count = min(16, mirror_count)
    matrix = [
    ["",  1, 2, 3, 4, ""],
    [15, "", "", "", "", 5],
    [14, "", "", "", "", 6],
    [13, "", "", "", "", 7],
    [12, "", "", "", "", 8],
    ["", 11, "L", 10, 9, ""]
  ]

    for i in range(mirror_count):
        r = [randint(1,4),randint(1,4)]
        while matrix[r[0]][r[1]] != "":
            r = [randint(1,4),randint(1,4)]
        matrix[r[0]][r[1]] = "/" if randint(0,1) else "\\"
    
    cells = matrix # position en [Y][X]
    lum_pos = [2,4] # position en [x,y] !!
    lum_dir = [0,-1]
    mirrors = {
        "/":-1,
        "\\":1
    }
    while 0 < lum_pos[0] < 5 and 0 < lum_pos[1] < 5:
        if mirrors.get(cells[lum_pos[1]][lum_pos[0]]):
            k=mirrors.get(cells[lum_pos[1]][lum_pos[0]])
            # lors contact miroir la direction (x,y) devient (y,x) * 1 ou -1 en fonction du miroir 
            lum_dir = [lum_dir[1]*k, lum_dir[0]*k] 
        lum_pos = [lum_pos[0] + lum_dir[0],lum_pos[1]+lum_dir[1]]
    # remplacer par dictionnaire plutôt que conditions ?
    if lum_pos[1] == 0: result =  lum_pos[0] 
    elif lum_pos[0] == 5: result =  lum_pos[1] + 4
    elif lum_pos[1] == 5: 
        if lum_pos[0] == 1:
            result =  11
        else:
            result =  13 - lum_pos[0]
    else: result =  16 - lum_pos[1]
    return matrix, result


def calcul(maxi=None):
    if maxi == None: maxi = randint(20,99)
    maxi = max(6,maxi)
    n = randint(1,maxi)
    n0 = n
    result = []
    numbers=[]
    for i in range(5):
        r = randint(1,n)
        k=0
        while (r in result or n-r in result or n-r == r): 
            r = randint(1,n)
            k+=1
        result.append(r)
        n -= r
        if n < 2:
            break
    if n != 0: result.append(n)
    numbers += result
    while len(numbers) < 6:
        r = randint(1,maxi)
        while r in numbers:
            r = randint(1,maxi)
        numbers.append(r)
    shuffle(numbers)
    return n0, numbers, "+".join(str(i) for i in result)

def manquant(maxi=None, size=None):
    if maxi == None: maxi = randint(10,99)
    if size == None: size = randint(5,100)
    red_len = randint(1,size-1)
    blue_len = size - red_len
    maxi = max(max(red_len, blue_len), maxi-max(red_len, blue_len))
    red_start, blue_start = randint(1,maxi), randint(1,maxi)
    red = [str(i)+"R" for i in range(red_start,red_start+red_len+1)]
    blue = [str(i)+"B" for i in range(blue_start,blue_start+blue_len+1)]
    if blue_len <= 2 or randint(0,1) and red_len > 2:
        r = randint(2,red_len-1)
        result = int(red[r][:-1])
        red[r]= str(red_start+red_len+1)+"R"
    else:
        r = randint(2,blue_len-1)
        result = int(blue[r][:-1])
        blue[r]= str(blue_start+blue_len+1)+"B"
    liste = (red + blue)
    shuffle(liste)
    return liste, result

def labyrinthe(size=None):
    if size == None: size = randint(5,30)
    size = max(5,min(size, 99))
    cols_length = size
    rows_length = size

    def bool_visited(row,col,pos):
        for x,y in directions:
            new_row = row + x
            new_col = col + y 
            if (
                0 <= new_row < rows_length
                and 0 <= new_col < cols_length
                and ((((new_row,new_col) in visited or (new_row,new_col) in start_pos)
                and pos != (new_row,new_col))
                or (not first and maze[new_col][new_row] == "D"))
            ):
                return False
        return True

    start_pos = [(0,0), (rows_length-1,0), (rows_length-1,cols_length-1), (0,cols_length-1)]
    maze = [["X"]*rows_length for i in range(cols_length)]
    for i,(row,col) in enumerate(start_pos):
        maze[col][row] = str(i+1)

    visited = set(start_pos)
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    first = True
    numbers =   [1, 2, 3, 4]
    r = randint(0,3)
    number = numbers.pop(r) 
    result = number
    row,col = start_pos.pop(r)
    queue = [(row,col)]
    maze[cols_length//2][rows_length//2] = "D"
    around_D = [maze[cols_length//2+1][rows_length//2],
            maze[cols_length//2-1][rows_length//2],
            maze[cols_length//2][rows_length//2+1],
            maze[cols_length//2][rows_length//2-1]]
    while "" not in around_D:
        start_pos = [(0,0), (rows_length-1,0), (rows_length-1,cols_length-1), (0,cols_length-1)]
        maze = [["X"]*rows_length for i in range(cols_length)]
        maze[cols_length//2][rows_length//2] = "D"
        for i,(row,col) in enumerate(start_pos):
            maze[col][row] = str(i+1)

        visited = set(start_pos)
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        first = True
        numbers =   [1, 2, 3, 4]
        r = randint(0,3)
        number = numbers.pop(r) 
        result = number
        row,col = start_pos.pop(r)
        queue = [(row,col)]
        while queue:
            possible = []
            for (x,y) in directions:
                new_row = row + x
                new_col = col + y
                if (
                        (new_row, new_col) not in visited
                        and 0 <= new_row < rows_length
                        and 0 <= new_col < cols_length
                        and bool_visited(new_row, new_col, (row,col))
                        and maze[new_col][new_row] in ("X","D")
                    ):
                    if maze[new_col][new_row] == "D":
                        break
                    possible.append((new_row, new_col))
            else:
                if possible:
                    r = randint(0,len(possible)-1)
                    row,col = possible[r]
                    maze[col][row] = ""
                    visited.add((row,col))
                    queue.append((row,col))
                else:
                    row,col = queue.pop()
                continue
            break
        around_D = [maze[cols_length//2+1][rows_length//2],
            maze[cols_length//2-1][rows_length//2],
            maze[cols_length//2][rows_length//2+1],
            maze[cols_length//2][rows_length//2-1]]
    first = False
    paths = []
    for number,(row,col) in zip(numbers,start_pos):
        queue = [(row,col)]
        paths.append([number, (row,col), queue])
    while paths:
        for i,[number, (row,col), queue] in enumerate(paths):
            possible = []
            for (x,y) in directions:
                new_row = row + x
                new_col = col + y
                if (
                        (new_row, new_col) not in visited
                        and 0 <= new_row < rows_length
                        and 0 <= new_col < cols_length
                        and bool_visited(new_row, new_col, (row,col))
                        and maze[new_col][new_row] in ("X","D")
                    ):
                    possible.append((new_row, new_col))
            if possible:
                r = randint(0,len(possible)-1)
                row,col = possible[r]
                maze[col][row] = ""
                visited.add((row,col))
                queue.append((row,col))
                paths[i] = [number, (row,col), queue]
            elif queue:
                row,col = queue.pop()
                paths[i] = [number, (row,col), queue]
            else:
                paths.pop(i)
    return maze, result
    
def raisonnement(size=None):
    if size == None: size = randint(5,30)
    drawing = []
    rows_length = size
    cols_length = size
    pieces = []
    number_piece = 3
    real_pieces = []
    for i in range(number_piece):
        piece_width = randint(3,rows_length)
        piece_height = randint(3,cols_length)
        piece = []
        real_piece = []
        space_in_first = False
        while not space_in_first:
            space_in_first = False
            for j in range(piece_height):
                ok = False
                while not ok:
                    row = []
                    real_row = []
                    for k in range(piece_width):
                        r = randint(0,1)
                        row.append("" if r < 1 else "X")
                        real_row.append("X" if r < 1 else "")
                    if "" in row:
                        ok = True
                piece.append(row)
                real_piece.append(real_row)
            for row in piece:
                if row[0] == "":
                    space_in_first = True
                    break
        pieces.append(piece)
        real_pieces.append(real_piece)

    r = randint(0,number_piece-1)
    piece = pieces[r]
    piece_width = len(piece[0])
    piece_height = len(piece)
    for i in range((cols_length-piece_height)//2):
        drawing.append(["X"]*rows_length)
    for i in range(piece_height):
        row = ["X"]*((rows_length-piece_width)//2)
        row+=piece[i]
        row += ["X"]*(rows_length-len(row))
        drawing.append(row)
    for i in range(((cols_length-piece_height)//2)+1):
        drawing.append(["X"]*rows_length)

    letters = ["A", "B", "C"]
    dict_pieces = {}
    for letter,piece in zip(letters,real_pieces):
        dict_pieces[letter]=piece
    result = letters[r]
    return drawing, dict_pieces, result

def get(type=None, *args):
    #si aucun argument concernant la taille des données est donné,
    #la taille est choisi aléatoirement par l'algo
    datatype={
        "couleur":"colors",
        "reflexion":"map",
        "calcul":["result", "numbers"],
        "frequence":"words",
        "manquant": "numbers",
        "labyrinthe": "map",
        "doublon": "words",
        "raisonnement": ["drawing", "pieces"]
    }
    try:
        func = globals()[type]
    except:
        return None
    if args:
        data = func(*args)
    else:
        data = func()
    card = {
        "code": "Test",
        "type": func.__name__,
    }
    if len(data)==2:
        card[datatype[func.__name__]] = data[0]

    else:
        for i,d in enumerate(data[:-1]):
            card[datatype[func.__name__][i]] = d
    result = data[-1]
    return card, result










# for i in range(100000):
#     if manquant()[1] > 99:
#         print("aaaaaaaaaaaaaaa")
#         break
# for i in range(1000):
#     c = calcul(99)
#     #print("____________________________________")
#     if c[0] != sum(c[2]) or len(c[2]) != len(set(c[2])) or len(set(c[1])) != 6:
#         print(f'\033[0;31m', end="")
#         print("FF")
#         break
# else:
#     print(f'\033[0;32m', end="")
#     print("Let's GO !")