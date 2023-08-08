
# class Graph:
#     def __init__(self) -> None:
#         self.graph = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.graph and vertex2 in self.graph:
#             self.graph[vertex1].append(vertex2)
#             self.graph[vertex2].append(vertex1)

#     def display(self):
#         for vertex, neghibors in self.graph.items():
#             print(vertex,"-->", ", ".join(neghibors))
    
    
            

# graph = Graph()
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")
# graph.add_vertex("E")


# graph.add_edge("A", "B")
# graph.add_edge("B", "C")
# graph.add_edge("C", "D")
# graph.add_edge("D", "E")
# graph.add_edge("E", "A")
# graph.display()


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

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for vertices in self.graph.values():
                if vertex in vertices:
                    vertices.remove(vertex)

    def delete_vedge(Self, vertex1, vertex2):
        if vertex1 in Self.graph and vertex2 in Self.graph:
            if vertex2 in Self.graph[vertex1]:
                Self.graph[vertex1].remove(vertex2)
            if vertex1 in Self.graph[vertex2]:
                Self.graph[vertex2].remove(vertex1)

    def display(self):
        for vertices, neghibors in self.graph.items():
            print(vertices,"-->"," , ".join(neghibors))

g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "A")

# g.delete_vedge("B","C")
# g.delete_vertex("A")
g.display()