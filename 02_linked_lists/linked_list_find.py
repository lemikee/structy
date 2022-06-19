# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
    if head is None:
        return False

    current = head

    while current:
        if current.val == target:
            return True
        current = current.next

    return False
    #   if head is None: return False

    #   if head.val == target: return True

    # #   if linked_list_find(head.next, target): return True

    # #   return False

    #   return linked_list_find(head.next, target)
