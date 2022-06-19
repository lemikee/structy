# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque


def bottom_right_value(root):
    # in python, for/while loops don't create local scopes
    # current = None
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return current.val
