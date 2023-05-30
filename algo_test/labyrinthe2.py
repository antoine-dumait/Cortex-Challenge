import time
M = [
    ["1", "X", "X", "X", "X", "X", "X", "", "", "2"],
    ["", "", "", "", "", "", "X", "", "X", ""],
    ["X", "X", "X", "X", "X", "", "X", "", "X", ""],
    ["X", "X", "X", "X", "X", "D", "X", "X", "X", ""],
    ["X", "X", "X", "", "", "X", "X", "", "", ""],
    ["X", "X", "X", "", "X", "X", "X", "", "X", "X"],
    ["4", "", "", "", "X", "X", "X", "", "", "3"]
  ]

M = [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "1", "", "", "X","X","X","X","X","X","X","X","X","X","X","X","X","X","X", "2", "X"],
    ["X", "", "X", "", "X", "", "", "", "", "", "", "", "", "", "", "", "", "X", "X", "", "X"],
    ["X", "", "X", "", "X", "", "X", "X", "X", "X", "X", "X", "", "", "X", "X", "X", "X", "X", "", "X"],
    ["X", "", "X", "", "X", "", "X", "", "", "", "", "", "X", "", "", "", "", "X", "X", "", "X"],
    ["X", "", "X", "", "X", "", "X", "", "X", "X", "X", "", "X", "X", "X", "X", "", "X", "X", "", "X"],
    ["X", "", "X", "X", "X", "X", "X", "", "X", "", "X", "", "", "", "", "X", "", "X", "X", "", "X"],
    ["X", "X", "", "", "", "", "", "", "X", "", "X", "", "", "X", "D", "X", "", "X", "X", "", "X"],
    ["X", "", "", "X", "X", "X", "X", "X", "X", "", "X", "X", "X", "X", "X", "X", "", "X", "X", "", "X"],
    ["X", "", "", "", "X", "X", "X", "X", "X", "", "X", "X", "X", "X", "X", "", "", "X", "X", "", "X"],
    ["X", "X", "X", "", "X", "", "", "", "", "", "X", "X", "X", "X", "X", "", "", "", "", "", "X"],
    ["X", "X", "X", "", "X", "", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "4", "", "", "X", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "3", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
  ]
b = M
stack = []
len_ligne = len(M[0])
len_colonne = len(M)

def draw_maze():
    print(f'\x1B[{len_colonne}A', end="")
    for y,l in enumerate(b):
            for x,j in enumerate(l):
                if j == "":
                    print(" ", end="")
                else: 
                    if len(j) > 1:
                        if [x,y] == pos: 
                            print(f'\033[0;3{bold_white}m', end="")
                        else: 
                            print(f'\033[0;3{j[1]}m', end="")
                        print(j[0], end="")
                    else:
                        if [x,y] == new_pos:
                            print(f'\033[0;3{cyan}m', end="")
                        print(j, end="")
                    print('\033[00m', end="")
            print()
    time.sleep(0.05)
    

def add_pos(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]

first = 2
last = 2
start_pos = [[M[first-1].index("1"),first-1],[M[first-1].index("2"),first-1], [M[len_colonne-last].index("3"),len_colonne-last], [M[len_colonne-last].index("4"), len_colonne-last]]
print(start_pos)
colors = [1,2,3,4]
purple = 5
cyan = 6
bold_white = 7
dirs = [[-1,0],[0,-1],[1,0],[0,1]]
visited = []
stack = []
paths = []
stucks = []
for i in range(5):
    print()
for i,(pos,color) in enumerate(zip(start_pos, colors)):
    paths.append({
        "color": color, 
        "pos": pos, 
        "stack": [pos],
        "visited": [pos]})
    stucks.append(i)
print(f'{len_ligne=}, {len_colonne=}')
print("\n\n")
k=0
while stucks != []:
    k+=1
    #print(stucks)
    for i in stucks:
        path = paths[i]
        pos = path["pos"]
        stack = path["stack"]
        color = path["color"]
        # for a in range(10):
        #     print()
        visited = path["visited"]
        if stack == []:
            stucks.remove(i)
            break
        #print(k,i,stack)
        for dir in dirs:
            new_pos = add_pos(pos, dir)
            draw_maze()
            if 0 <= new_pos[0] < len_ligne and 0 <= new_pos[1] < len_colonne and new_pos not in visited and M[new_pos[1]][new_pos[0]] != "X":
                if M[new_pos[1]][new_pos[0]] == "":
                    path["pos"] = new_pos
                    b[pos[1]][pos[0]] = (".",color)
                    stack.append(pos)
                    visited.append(pos)
                    break
                elif M[new_pos[1]][new_pos[0]] == "D":
                    path["pos"] = new_pos
                    b[pos[1]][pos[0]] = ("!",color)
                    stack.append(pos)
                    visited.append(pos)
                    break
                else:
                    path["pos"] = new_pos
                    b[pos[1]][pos[0]] = M[new_pos[1]][new_pos[0]]
                    stack.append(pos)
                    visited.append(pos)
        else:
            path["pos"] = stack.pop()