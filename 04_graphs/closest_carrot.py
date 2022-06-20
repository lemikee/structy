from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    visited = set([(starting_row, starting_col, 0)])
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        r, c, level_num = queue.popleft()

        if grid[r][c] == 'C':
            return level_num

        deltas = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        for delta in deltas:
            delta_row, delta_col = delta
            new_row = r + delta_row
            new_col = c + delta_col
            new_pos = (new_row, new_col)
            row_inbound = 0 <= new_row < len(grid)
            col_inbound = 0 <= new_col < len(grid[0])

            if row_inbound and col_inbound and new_pos not in visited and grid[new_row][new_col] != 'X':
                visited.add(new_pos)
                queue.append((new_row, new_col, level_num + 1))

    return -1
