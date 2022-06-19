# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque


def tree_levels(root):
    # pass # todo

    if root is None:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        current, level_num = queue.popleft()

        if 0 <= level_num < len(levels):
            levels[level_num].append(current.val)
        else:
            # levels.insert(level_num, [ current.val ])
            levels.append([current.val])

        if current.left:
            queue.append((current.left, level_num + 1))
        if current.right:
            queue.append((current.right, level_num + 1))

    return levels
