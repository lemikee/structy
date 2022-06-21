def subsets(elements, i=0):
    if i >= len(elements):
        return [[]]

    element = elements[i]

    subsets_without = subsets(elements, i + 1)
    subsets_with = [[*subset, element] for subset in subsets_without]

#   for subset in subsets_without:
#     subsets_with.append( [*subset, element] )

    return [*subsets_with, *subsets_without]
