# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
    if head is None:
        return False

    current = head

    while current:
        if current.val != head.val:
            return False
        current = current.next

    return True

# ptrs
#   current - tracks current node in linked list
#   head - points to head of linked list

# traverse through linked list
#   if current node's value is NOT equal to head's value, return False
#   move current ptr forward

# return True
