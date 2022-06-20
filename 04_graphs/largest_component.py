def largest_component(graph):
    largest = 0
    visited = set()

    for node in graph:
        size = explore_size(graph, node, visited)
        if size > 0:
            largest = max(largest, size)

    return largest


def explore_size(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)

    size = 1

    for neighbor in graph[current]:
        size += explore_size(graph, neighbor, visited)

    return size
