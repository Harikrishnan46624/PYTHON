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

    def display(self):
        for vertex,neghibours in self.graph.items():
            print(vertex,"-->", ", ".join(neghibours))

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for vertices in self.graph.values():
                if vertex in vertices:
                    vertices.remove(vertex)

    def delete_edge(Self, vertex1, vertex2):
        if vertex1 in Self.graph and vertex2 in Self.graph:
            if vertex2 in Self.graph[vertex1]:
                Self.graph[vertex1].remove(vertex2)
            if vertex1 in Self.graph[vertex2]:
                Self.graph[vertex2].remove(vertex1)


graph = Graph()

# Add vertices to the graph
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

# Add edges between vertices
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
graph.add_edge("E", "A")

# Display the graph
graph.display()

# graph.delete_vertex("C")

# Delete an edge
graph.delete_edge("A", "B")

# Display the updated graph
print("Deleted")
graph.display()



