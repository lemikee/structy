# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]

    left_leaves = leaf_list(root.left)
    right_leaves = leaf_list(root.right)

    return [*left_leaves, *right_leaves]
