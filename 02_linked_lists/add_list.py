class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists(head_1, head_2):
    dummy_head = Node(None)
    current_1 = head_1
    current_2 = head_2
    tail = dummy_head
    carry = 0

    while current_1 is not None or current_2 is not None or carry == 1:
        val_1 = current_1.val if current_1 else 0
        val_2 = current_2.val if current_2 else 0
        sum = val_1 + val_2 + carry
        digit = sum if sum < 10 else sum % 10
        carry = 0 if sum < 10 else 1

        tail.next = Node(digit)
        tail = tail.next

        if current_1:
            current_1 = current_1.next
        if current_2:
            current_2 = current_2.next

    return dummy_head.next
