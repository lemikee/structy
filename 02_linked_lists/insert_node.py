class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node

    current = head
    count = 0

    while current:
        if count + 1 == index:
            new_node = Node(value)
            next = current.next
            current.next = new_node
            new_node.next = next
            return head
        current = current.next
        count += 1

    return head

# when we are right before the index that we want to insert the node at
#   we create a node with the appropriate value, get current node's next
#   have current node's next be new node, and new node's ptr be next node we prev saves

# edge case: index is 0
#   create node with value
#   have node's next be head
#   return new node

# ptrs
#   current
#   count - tracks index of current node

# traverse through linked list
#   if count + 1 == index
#     we are right before the index where we want to insert the new node
#     create a new node with value
#     save current's next to new ptr - next
#     have current's next be new node
#     have new node's ptr be next
#     return head
#   move current's ptr forward
#   increment count
#
#   return head
