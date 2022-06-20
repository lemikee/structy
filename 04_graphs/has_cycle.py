def has_cycle(graph):
    visiting = set()
    visited = set()

    for node in graph:
        if node not in visited:
            if detect_cycle(graph, node, visited, visiting):
                return True

    return False


def detect_cycle(graph, node, visited, visiting):
    if node in visited:
        return False
    if node in visiting:
        return True
    visiting.add(node)

    for neighbor in graph[node]:
        if detect_cycle(graph, neighbor, visited, visiting):
            return True

    visited.add(node)
    return False
