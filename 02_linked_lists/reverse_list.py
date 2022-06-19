def reverse_list(head):
    if head is None:
        return None

    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

        # save current's next, otherwise will lose it when we change current's next to prev
        # change current's next to be prev

    return prev
