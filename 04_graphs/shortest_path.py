from collections import deque


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:
        current, level_num = queue.popleft()

        if current == node_B:
            return level_num

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, level_num + 1))
                visited.add(neighbor)

    return -1


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
