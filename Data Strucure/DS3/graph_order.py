class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start_vertex, visited = None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex)
        for neighbour in self.graph[start_vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited,)

graph = Graph()

# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Perform BFS traversal starting from 'A'
print("BFS Traversal:")
graph.bfs('A')

print("DFS Traversal:")
graph.dfs('A')