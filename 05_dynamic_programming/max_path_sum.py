def _max_path_sum(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])

    if not row_inbound or not col_inbound:
        return 0
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    left_max_sum = _max_path_sum(grid, r, c + 1, memo)
    down_max_sum = _max_path_sum(grid, r + 1, c, memo)

    memo[pos] = grid[r][c] + max(left_max_sum, down_max_sum)
    return memo[pos]


def max_path_sum(grid):
    memo = {}
    return _max_path_sum(grid, 0, 0, memo)
