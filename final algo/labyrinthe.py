from collections import deque

def main(card :dict):
    maze = card.get("map")
    cols_length = len(maze)
    rows_length = len(maze[0])

    for y,row in enumerate(maze):
        try:
            start_row = row.index("D")
            start_col = y
            break
        except: 
            pass
        
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])

    while queue:
        row, col = queue.popleft()
        if maze[col][row] in ["1", "2", "3", "4"]:
            return int(maze[col][row])
        for d in directions:
            new_row = row + d[0]
            new_col = col + d[1]
            if (
                (new_row, new_col) not in visited
                and 0 <= new_row < rows_length
                and 0 <= new_col < cols_length
                and maze[new_col][new_row] != "X"
            ):
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))