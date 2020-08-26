from graph import Graph as G


class Graph(G):
    def generate_dft_paths(self, starting_node, path=[]):
        path = path + [starting_node]

        unvisited_neighbors = self.get_neighbors(starting_node)

        if len(unvisited_neighbors) < 1:
            yield path
        else:
            for unvisited_neighbor in unvisited_neighbors:
                yield from self.generate_dft_paths(unvisited_neighbor, path)

    def get_dft_paths(self, starting_node):
        return list(self.generate_dft_paths(starting_node))


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # Add vertices
    for pair in ancestors:
        if not pair[0] in graph.vertices:
            graph.add_vertex(pair[0])
        if not pair[1] in graph.vertices:
            graph.add_vertex(pair[1])

    # Add edges
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    paths = graph.get_dft_paths(starting_node)

    if len(paths) == 1 and len(paths[0]) == 1:
        return -1

    longest_path = -1
    ancestor = starting_node

    for path in paths:
        if len(path) > longest_path:
            longest_path = len(path)
            ancestor = path[-1]

        elif len(path) == longest_path:
            if path[-1] < ancestor:
                ancestor = path[-1]
    return ancestor


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 2))
