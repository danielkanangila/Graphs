"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] if vertex_id in self.vertices else None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to track visited vertices.
        visited = set()
        # Create a queue for BFS and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            # get the currect vertex and dequeue from queue and print it
            current_vertex = queue.dequeue()
            visited.add(current_vertex)
            print(current_vertex)

            # if current_vertex not in visited:
            # Get all adjacent vertices of the current_vertex
            # check if a adjacent vertex has not been visited
            # if not mark if as visited and enqueue it to the queue
            for neighbor in self.get_neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            last_vertex = stack.pop()

            if last_vertex not in visited:
                print(last_vertex)
                visited.add(last_vertex)

                for neighbor in self.get_neighbors(last_vertex):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        current_vertex = starting_vertex

        if current_vertex not in visited:
            print(current_vertex)
            visited.add(current_vertex)

            for neighbor in self.get_neighbors(current_vertex):
                self.dft_recursive(neighbor, visited=visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue, enqueue the starting vertex
        # and create a empty visited set to track visited vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size() > 0:
            # Dequeue the first PATH and get the vertex from the end of the path
            path = queue.dequeue()
            current_vertex = path[-1]

            # check if current visited has been visited
            # mark it visitied if not
            if current_vertex not in visited:
                visited.add(current_vertex)
                # check if the current equal to the target, if yes return the path
                if current_vertex == destination_vertex:
                    return path
                # Get all current_vertex neighbors and enqueue them to the que
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            last_vertex = path[-1]

            if last_vertex not in visited:
                visited.add(last_vertex)

                if last_vertex == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(last_vertex):
                    new_path = list(path)
                    new_path.append(neighbor)

                    stack.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        if starting_vertex not in self.vertices:
            return None
        shortest_path = None

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in path:
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path

        return shortest_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
