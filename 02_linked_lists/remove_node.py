# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
    if head.val == target_val:
        return head.next

    prev = None
    current = head

    while current:
        if current.val == target_val:
            next = current.next
            prev.next = next
            return head

        prev = current
        current = current.next

    return head

# if head.val == target_val: return head.next

# ptrs
#   prev - tracks previous node, initally set to None
#   current - tracks current node during traversal

# traverse through linked list
#   if current.val is equal to target_val
#     get current's next and save to variable - next
#     change prev's ptr to next
#     return head
#   move prev and current ptr's forward
#   prev = current
#   current = current.next
#
#  return head
