def island_count(grid):
    count = 0
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if find_island(grid, r, c, visited):
                count += 1

    return count


def find_island(grid, r, c, visited):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])
    pos = (r, c)

    if not row_inbound or not col_inbound:
        return False
    if pos in visited:
        return False
    visited.add(pos)
    if grid[r][c] == 'W':
        return False

    find_island(grid, r + 1, c, visited)
    find_island(grid, r - 1, c, visited)
    find_island(grid, r, c + 1, visited)
    find_island(grid, r, c - 1, visited)

    return True

# need some iterative code traverse through each position of the grid graph
# used nested loops to explore each position
# visited set
# count

# dfs on each island
