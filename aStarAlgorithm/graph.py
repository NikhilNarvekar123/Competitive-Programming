from vertex import Vertex

class Graph:

    def __init__(self):
        self.vertices = []

    def add_vertex(self, *args):
        for arg in args:
            self.vertices.append(arg)

    def clear_graph(self):
        self.vertices = []

    def get_vertices(self) -> list:
        returnArr = []
        for vertex in self.vertices:
            returnArr.append(vertex)
        return returnArr

    def show_graph(self):
        for vertex in self.vertices:
            disp = vertex.get_name()
            disp += " -> " + vertex.display_adjacent_vertices()
            print(disp)
