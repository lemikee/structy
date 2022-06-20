def longest_path(graph):
    distance = {}

    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        find_distance(graph, node, distance)

    return max(distance.values())


def find_distance(graph, current, distance):
    if current in distance:
        return distance[current]

    farthest = 0

    for neighbor in graph[current]:
        attempt = find_distance(graph, neighbor, distance)
        farthest = max(farthest, attempt)

    distance[current] = farthest + 1
    return distance[current]


#  initialize a dictionary, distance, where keys are nodes, and values are distance to farthest
#  terminal node

# find terminal nodes are put them in distance dictionary w/ value of 0
# iterative code - not guaranteed a single component in our graph

# helper function to help actually drive DFS recursion

# return longest value in distance
