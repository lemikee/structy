# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
    if root is None:
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.val, *left_values, *right_values]
    #   if root is None: return []

    #   stack = [ root ]
    #   values = []

    #   while stack:
    #     current = stack.pop()
    #     values.append(current.val)

    #     if current.right: stack.append(current.right)
    #     if current.left: stack.append(current.left)

    #   return values
