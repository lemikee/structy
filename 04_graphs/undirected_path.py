def undirected_path(edges, node_A, node_B):
    if node_A == node_B:
        return True
    graph = build_graph(edges)
    visited = set()
    result = has_path(graph, node_A, node_B, visited)
    return result


def has_path(graph, node_A, node_B, visited):
    if node_A in visited:
        return False
    visited.add(node_A)

    if node_A == node_B:
        return True

    for neighbor in graph[node_A]:
        if has_path(graph, neighbor, node_B, visited):
            return True

    return False


def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph
