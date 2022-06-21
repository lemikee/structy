def _count_paths(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])

    if not row_inbound or not col_inbound:
        return 0
    if grid[r][c] == 'X':
        return 0
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    left_paths = _count_paths(grid, r, c + 1, memo)
    down_paths = _count_paths(grid, r + 1, c, memo)

    memo[pos] = left_paths + down_paths
    return memo[pos]

#   DFS recursion


def count_paths(grid):
    memo = {}
    return _count_paths(grid, 0, 0, memo)
