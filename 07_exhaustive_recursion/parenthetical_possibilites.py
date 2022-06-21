def parenthetical_possibilities(s):
    if len(s) == 0:
        return ['']

    remainder, choices = get_options(s)
    suffixes = parenthetical_possibilities(remainder)
    possibilites = []

    for suffix in suffixes:
        possibilites += [choice + suffix for choice in choices]

    return possibilites


def get_options(s):
    if s[0] == '(':
        end = s.index(')')
        remainder = s[end + 1:]
        choices = s[1:end]
        return (remainder, choices)
    else:
        # return (s[0], s[1:])
        chars = s[0]
        remaining = s[1:]
        return (s[1:], s[0])

# def get_options(s):
#   if s[0] == '(':
#     idx = s.index(')')
#     chars = s[1:idx]
#     remaining = s[idx + 1:]
#     return ( remaining, chars )
#   else:
#     chars = s[0]
#     remaining = s[1:]
#     return ( remaining, chars )
