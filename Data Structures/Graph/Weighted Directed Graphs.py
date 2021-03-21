class WeightedGraph:
    def __init__(self, edges):
        """
        Transform a list of edges in a dictionary with keys: starting points, values: end points.

        :param edges: Le das al objeto todos los caminos existentes bajo forma de lista
        """
        self.edges = edges
        self.graph_dict = {}
        self.nodes = []
        for start, end, weight in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append((end, weight))
            else:
                self.graph_dict[start] = [(end, weight)]
            if start not in self.nodes:
                self.nodes.append(start)
            if end not in self.nodes:
                self.nodes.append(end)
        print("Graph Dict:", self.graph_dict)

    def shortest_path_Belman_Ford(self, starting_vertex="S"):
        if starting_vertex not in self.graph_dict:
            raise Exception("Not this node in the graph")
        distances = dict()
        for u in self.graph_dict:
            if u == starting_vertex:
                distances[u] = 0
            else:
                distances[u] = float("inf")
        counter_iterations = 0
        while counter_iterations < len(list(self.graph_dict)) - 1:
            counter_iterations += 1
            for node, starting_edges in self.graph_dict.items():
                for edge in starting_edges:
                    distances[edge[0]] = min(distances[edge[0]], distances[node] + edge[1])
        return distances


if __name__ == "__main__":
    Graph_List = [
        ("S", "E", 8), ("S", "A", 10), ("A", "C", 2), ("E", "D", 1), ("D", "A", -4), ("D", "C", -1),
        ("C", "B", -2), ("B", "A", 1)
    ]
    Example_Graph = WeightedGraph(Graph_List)
    print(Example_Graph.shortest_path_Belman_Ford())