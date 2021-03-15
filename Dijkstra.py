import numpy as np


def selectMinDistanceVortex(distances, processed):
    distances_ = distances
    distances_[processed == 1] = float("inf")
    return np.argmin(distances_)


def dijkstra(graph, goal_node):
    """

    :param graph: Weight matrix
    :param goal_node: Which node are we willing to achieve in minimum time
    :return: Minimum path using Dijkstra's algorithm
    """
    total_nodes = np.shape(graph)[0]  # How many nodes does our graph have
    parent = np.array([-1 for j in range(total_nodes)])  # Parents array
    distances = np.zeros(total_nodes)  # Initialized tentative distances
    processed = np.zeros(total_nodes)  # Which nodes have been processed
    for i in range(1, total_nodes):
        distances[i] = float("inf")  # Every distance to infinity except for initial node
    while processed[goal_node] == 0:  # While goal node hasn't been processed we keep going
        u = selectMinDistanceVortex(distances, processed)
        processed[u] = 1
        for j in range(total_nodes):
            if (graph[u, j] != 0) & (processed[j] == 0) & (distances[j] > distances[u] + graph[u, j]):
                distances[j] = distances[u] + graph[u, j]
                parent[j] = u
    path = []
    path_node = goal_node  # Creating optimal path list
    while path_node != 0:
        path.append(path_node)
        path_node = parent[path_node]
    path.reverse()
    return path
