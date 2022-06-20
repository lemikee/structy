def connected_components_count(graph):
    count = 0
    visited = set()

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True
