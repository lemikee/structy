# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
    head = head_1
    current_1 = head_1.next
    current_2 = head_2
    tail = head
    count = 0

    while current_1 and current_2:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        count += 1
        tail = tail.next

    if current_1:
        tail.next = current_1
    if current_2:
        tail.next = current_2

    return head


#   choose head_1 to be the new head of our zippered linked list
#   we'll return head_1

#   ptrs
#     current_1 - points to current node for head_1 linked list
#     current_2 - points to current node for head_2 linked list
#     tail - points to current tail of our new linked list
#     count - used to decide which node to append to out new linked list

#   traverse through our two linked lists while both are not None
#     if count is even
#       append current_2 to tail
#       move current_2 ptr forward
#     else
#       append current_1 to tail
#       move current_1 ptr forward
#     increment count
#     move tail ptr forward

#     may have case where both linked lists we take in are NOT the same length
#     append the rest of the linked list that has not been traversed through to tail of new LL


#   return head_1
