class Graph:
    def __init__(self, edges):
        """
        Transform a list of edges in a dictionary with keys: starting points, values: end points.

        :param edges: Le das al objeto todos los caminos existentes bajo forma de lista
        """
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        """
        Encuentra todos los caminos entre start y end

        :param start:
        :param end:
        :param path: El camino que se va recogiendo.

        :return: Lista de listas con los caminos posibles.

        """
        path = path + [start]

        if start == end:
            return [path]  # Para cuando lleguemos ya porfin recursivamente al destino deseado.

        if start not in self.graph_dict:
            return []

        paths = []  # Inicializamos la recursion.
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)  # Todos los caminos desde el vecino hasta el origen.
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))
