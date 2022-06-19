# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
    current_streak = 0
    best_streak = 0
    current_streak_val = None
    current = head

    while current:
        if current.val != current_streak_val:
            current_streak = 1
            current_streak_val = current.val
        else:
            current_streak += 1

        current = current.next
        best_streak = max(best_streak, current_streak)

    return best_streak

#   ptrs
#     current_streak
#     best_streak
#     current_streak_val
#     current

# traverse through linked list
#     if current's val is NOT equal to current_streak_val
#       then we must be on a new streak
#       so reset current_streak to 1
#       have current_streak_val to be current's val
#     else
#       we must be continuing our streak
#       so increment current_streak_val
#     choose best_streak to be the larger of best_streak and current_streak
#
#  return best_streak
