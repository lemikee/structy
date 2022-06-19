# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
    if root is None:
        return float('inf')

    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

    #   if root is None: return None

    #   stack = [ root ]
    #   min_val = float('inf')

    #   while stack:
    #     current = stack.pop()
    #     min_val = min(current.val, min_val)

    #     if current.left: stack.append(current.left)
    #     if current.right: stack.append(current.right)

    #   return min_val
