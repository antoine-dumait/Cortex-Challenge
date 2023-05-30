from collections import deque

def main(card :dict):
    # Get the dimensions of the maze
    maze = card.get("map")
    cols_length = len(maze)
    rows_length = len(maze[0])

    # Define the directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize the queue
    queue = deque([(0,0,1), (rows_length-1,0,2), (cols_length-1,cols_length-1,3), (0,cols_length-1,4)])

    # Initialize the visited set
    visited = set([(0,0,1), (rows_length-1,0,2), (cols_length-1,cols_length-1,3), (0,cols_length-1,4)])

    # Search for the exit
    while queue:
        row, col, path = queue.popleft()

        # Check if we've found the exit

        # Explore the neighboring cells
        for x,y in directions:
            new_row = row + x
            new_col = col + y

            # Check if the new cell is valid
            if (
                (new_row, new_col, path) not in visited
                and 0 <= new_row < rows_length
                and 0 <= new_col < cols_length
                and maze[new_col][new_row] in ("","D")
            ):
                if maze[new_col][new_row] == "D":
                    return path
                queue.append((new_row, new_col, path))
                visited.add((new_row, new_col, path))