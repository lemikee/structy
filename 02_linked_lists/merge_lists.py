class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    current_1 = head_1
    current_2 = head_2
    tail = dummy_head

    while current_1 and current_2:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next

        if current_1:
            tail.next = current_1
        if current_2:
            tail.next = current_2

    return dummy_head.next


#   use dummy_head pattern when choice of/for first node is UNCLEAR
#   create dummy node with value of None
#   --> BUT return dummy_head.next <-- important!

#  create dummy_head node with value of None
# ptrs
#   current_1 - tracks current node for head_1 linked list
#   current_2 - tracks current node for head_2 linked list
#   tail - tracks tail of new linked list, initally points to dummy_head

# traverse linked lists while current_1 and current_2 are BOTH not None
#   if current_1.val is less than current_2.val
#     then we choose current_1 to be appended to new linked list
#     move current_1 ptr forward
#   else
#     we choose current_2 to be appended to new linked list
#     move current_2 ptr forward
#   move tail ptr forward

#   we may have the case where the two linked lists we take in are NOT the same length
#   so append the rest of the longer linked list to our new linked list, if this is the case

#   return dummy_head.next
