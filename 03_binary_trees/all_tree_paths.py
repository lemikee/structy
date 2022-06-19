# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]

    leaves = []

    left_paths = all_tree_paths(root.left)
    for path in left_paths:
        new_path = [root.val, *path]
        leaves.append(new_path)

    right_paths = all_tree_paths(root.right)
    for path in right_paths:
        new_path = [root.val, *path]
        leaves.append(new_path)

    return leaves
