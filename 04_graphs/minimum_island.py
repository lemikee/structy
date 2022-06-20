def minimum_island(grid):
    min_size = float('inf')
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = find_island(grid, r, c, visited)
            if size > 0:
                min_size = min(min_size, size)

    return min_size


def find_island(grid, r, c, visited):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])
    if not row_inbound or not col_inbound:
        return 0
    pos = (r, c)

    if pos in visited:
        return 0
    visited.add(pos)

    if grid[r][c] == 'W':
        return 0

    size = 1

    size += find_island(grid, r + 1, c, visited)
    size += find_island(grid, r - 1, c, visited)
    size += find_island(grid, r, c + 1, visited)
    size += find_island(grid, r, c - 1, visited)

    return size
