from vertex import Vertex

class Graph:

    def __init__(self):
        self.vertices = []

    def add_vertex(self, *args):
        for arg in args:
            self.vertices.append(arg)

    def clear_graph(self):
        self.vertices = []

    def show_graph(self):
        for vertex in self.vertices:
            disp = vertex.get_name()
            disp += " -> " + vertex.display_adjacent_vertices()
            print(disp)

a = Vertex(0,"A")
b = Vertex(0, "B")
c = Vertex(0, "C")
d = Vertex(0, "D")
e = Vertex(0, "E")
f = Vertex(0, "F")
g = Vertex(0, "G")

a.set_adjacent_vertices((b,4), (c,3))
b.set_adjacent_vertices((e,12), (a,4), (f,5))
c.set_adjacent_vertices((a,3), (d,7), (e,10))
d.set_adjacent_vertices((c,7), (e,2))
e.set_adjacent_vertices((c,10), (b,12), (d,2), (g,5))
f.set_adjacent_vertices((b,5), (g,16))
g.set_adjacent_vertices((f,16), (e,5))

graph = Graph()
graph.add_vertex(a,b,c,d,e,f,g)
graph.show_graph()
