class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(values):
    dummy_head = Node(None)
    tail = dummy_head

    for value in values:
        new_node = Node(value)
        tail.next = new_node
        tail = tail.next

    return dummy_head.next

# create a dummy_head with value of None
# ptr
#   tail - tracks tail of new linked list

# iterate through values
#   create a new node for each value
#   append node to tail of new linked list
#   move tail ptr forward
#
# return dummy_head.next
