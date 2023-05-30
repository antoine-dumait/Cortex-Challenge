def main(card :dict):
    # Get the dimensions of the maze
    maze = card.get("map")
    cols_length = len(maze)
    rows_length = len(maze[0])

    # Find the starting position
    for i in range(cols_length):
        for j in range(rows_length):
            if maze[j][i] == "D":
                start_row = i
                start_col = j

    # Define the directions
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # Initialize the queue
    queue = [(start_row, start_col)]

    # Initialize the visited set
    visited = set([(start_row, start_col)])

    # Search for the exit
    while queue:
        row, col = queue.pop(0)

        # Check if we've found the exit
        if maze[col][row] in ["1", "2", "3", "4"]:
            return int(maze[col][row])

        # Explore the neighboring cells
        for d in directions:
            new_row = row + d[0]
            new_col = col + d[1]

            # Check if the new cell is valid
            if (
                (new_row, new_col) not in visited
                and 0 <= new_row < rows_length
                and 0 <= new_col < cols_length
                and maze[new_col][new_row] != "X"
            ):
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))