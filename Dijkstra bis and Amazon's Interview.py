import numpy as np


def dijkstra_bis(graph, start, goal):
    """

    :type goal: str
    """
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = float("inf")
    path = []
    for node in unseenNodes:
        if node != start:
            shortest_distance[node] = infinity
        else:
            shortest_distance[node] = 0
    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        path_options = graph[min_distance_node].items()
        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
        unseenNodes.pop(min_distance_node)

        ###############Algoritmo terminado : recorrer camino optimo.
    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = track_predecessor[current_node]
        except KeyError:
            print("Doesn't find an optimal path")
            break
    return shortest_distance[goal], path


def transform_amazon_array_to_graph(areas_to_deliver):
    graph = {}
    rows = areas_to_deliver.shape[0]
    columns = areas_to_deliver.shape[1]
    for row in range(rows):
        for column in range(columns):
            element = areas_to_deliver[row, column]
            if element == 0:
                graph[str((row, column))] = {}
            elif element == 1 or element == 9:
                graph[str((row, column))] = {}
                if element == 9:
                    goal_node = str((row, column))
                ########################## CASO NORMAL: EL ELEMENTO QUE RECORREMOS ESTA EN EL CENTRO DE LA MATRIZ.
                if row != 0 and (row + 1) != rows and column != 0 and (column + 1) != columns:

                    # Buscar abajo, arriba, izquierda y derecha.
                    # Izquierda
                    if areas_to_deliver[row, column - 1] == 1 or areas_to_deliver[row, column - 1] == 9:
                        graph[str((row, column))][str((row, column - 1))] = 1

                    # Derecha
                    if areas_to_deliver[row, column + 1] == 1 or areas_to_deliver[row, column + 1] == 9:
                        graph[str((row, column))][str((row, column + 1))] = 1

                    # Abajo
                    if areas_to_deliver[row + 1, column] == 1 or areas_to_deliver[row + 1, column] == 9:
                        graph[str((row, column))][str((row + 1, column))] = 1

                    # Arriba
                    if areas_to_deliver[row - 1, column] == 1 or areas_to_deliver[row - 1, column] == 9:
                        graph[str((row, column))][str((row - 1, column))] = 1

                ########################### CASO ESPECIAL: LIMITES DE LA MATRIZ

                if column == 0 and row != 0 and (row + 1) != rows:
                    # Derecha, abajo, arriba

                    # Derecha
                    if areas_to_deliver[row, column + 1] == 1 or areas_to_deliver[row, column + 1] == 9:
                        graph[str((row, column))][str((row, column + 1))] = 1

                    # Abajo
                    if areas_to_deliver[row + 1, column] == 1 or areas_to_deliver[row + 1, column] == 9:
                        graph[str((row, column))][str((row + 1, column))] = 1

                    # Arriba
                    if areas_to_deliver[row - 1, column] == 1 or areas_to_deliver[row - 1, column] == 9:
                        graph[str((row, column))][str((row - 1, column))] = 1

                if (column + 1) == columns and row != 0 and (row + 1) != rows:
                    # Izquierda, abajo, arriba

                    # Izquierda
                    if areas_to_deliver[row, column - 1] == 1 or areas_to_deliver[row, column - 1] == 9:
                        graph[str((row, column))][str((row, column - 1))] = 1

                    # Abajo
                    if areas_to_deliver[row + 1, column] == 1 or areas_to_deliver[row + 1, column] == 1:
                        graph[str((row, column))][str((row + 1, column))] = 1

                    # Arriba
                    if areas_to_deliver[row - 1, column] == 1 or areas_to_deliver[row - 1, column] == 9:
                        graph[str((row, column))][str((row - 1, column))] = 1

                if row == 0 and column != 0 and (column + 1) != columns:
                    # Izquierda, derecha, abajo

                    # Izquierda
                    if areas_to_deliver[row, column - 1] == 1 or areas_to_deliver[row, column - 1] == 9:
                        graph[str((row, column))][str((row, column - 1))] = 1

                    # Derecha
                    if areas_to_deliver[row, column + 1] == 1 or areas_to_deliver[row, column + 1] == 9:
                        graph[str((row, column))][str((row, column + 1))] = 1

                    # Abajo
                    if areas_to_deliver[row + 1, column] == 1 or areas_to_deliver[row + 1, column] == 9:
                        graph[str((row, column))][str((row + 1, column))] = 1

                if (row + 1) == rows and column != 0 and (column + 1) != columns:
                    # Izquierda derecha arriba

                    # Izquierda
                    if areas_to_deliver[row, column - 1] == 1 or areas_to_deliver[row, column - 1] == 9:
                        graph[str((row, column))][str((row, column - 1))] = 1

                    # Derecha
                    if areas_to_deliver[row, column + 1] == 1 or areas_to_deliver[row, column + 1] == 9:
                        graph[str((row, column))][str((row, column + 1))] = 1

                    # Arriba
                    if areas_to_deliver[row - 1, column] == 1 or areas_to_deliver[row - 1, column] == 9:
                        graph[str((row, column))][str((row - 1, column))] = 1

                ################################# CASO ESPECIAL: ESQUINAS

                if row == 0 and column == 0:

                    # Abajo
                    if areas_to_deliver[row + 1, column] == 1 or areas_to_deliver[row + 1, column] == 9:
                        graph[str((row, column))][str((row + 1, column))] = 1

                    # Derecha
                    if areas_to_deliver[row, column + 1] == 1 or areas_to_deliver[row, column + 1] == 9:
                        graph[str((row, column))][str((row, column + 1))] = 1

                if row == 0 and (column + 1) == columns:

                    # Abajo
                    if areas_to_deliver[row + 1, column] == 1 or areas_to_deliver[row + 1, column] == 9:
                        graph[str((row, column))][str((row + 1, column))] = 1

                    # Izquierda
                    if areas_to_deliver[row, column - 1] == 1 or areas_to_deliver[row, column - 1] == 9:
                        graph[str((row, column))][str((row, column - 1))] = 1

                if (row + 1) == rows and column == 0:
                    # Arriba
                    if areas_to_deliver[row - 1, column] == 1 or areas_to_deliver[row - 1, column] == 9:
                        graph[str((row, column))][str((row - 1, column))] = 1
                    # Derecha
                    if areas_to_deliver[row, column + 1] == 1 or areas_to_deliver[row, column + 1] == 9:
                        graph[str((row, column))][str((row, column + 1))] = 1

                if (row + 1) == rows and (column + 1) == columns:

                    # Arriba
                    if areas_to_deliver[row - 1, column] == 1 or areas_to_deliver[row - 1, column] == 9:
                        graph[str((row, column))][str((row - 1, column))] = 1

                    # Izquierda
                    if areas_to_deliver[row, column - 1] == 1 or areas_to_deliver[row, column - 1] == 9:
                        graph[str((row, column))][str((row, column - 1))] = 1
    # ELiminamos los lugares sin conexion
    for node in list(graph):
        if not graph[node]:
            graph.pop(node)

    return graph, goal_node


if __name__ == "__main__":
    areas_to_deliver = np.array([[1, 0, 1], [1, 0, 0], [1, 9, 1]])
    areas_to_deliver_complicated = np.array(
        [[1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 1, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 1, 9, 0]])
    print(areas_to_deliver_complicated)
    (graph_to_deliver, goal_node) = transform_amazon_array_to_graph(areas_to_deliver_complicated)
    (minimum_distance, path) = dijkstra_bis(graph_to_deliver, start="(0, 0)",
                                    goal=goal_node)
    print(f"The minimum distance to delivery zone is: {minimum_distance}")
    print(f"And the path he has to take is: {path}")
