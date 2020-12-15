
class Vertex:

    def __init__(self, value, name="node"):
        self.value = value
        self.name = name
        self.adjacentVertices = []
        self.heuristic_dist = 0

    def set_adjacent_vertices(self, *args):
        for arg in args:
            self.adjacentVertices.append(arg)

    def set_heuristic_dist(self, dist : int):
        self.heuristic_dist = dist

    def get_value(self) -> int:
        return self.value

    def get_name(self) -> str:
        return self.name

    def get_adjacent_vertices(self) -> list:
        vertices = []
        for vertex in self.adjacentVertices:
            vertices.append(vertex[0])
        return vertices

    def display_adjacent_vertices(self) -> str:
        dispStr = ''
        for i in range(len(self.adjacentVertices)):
            vertex = self.adjacentVertices[i]
            dispStr += '(' + vertex[0].get_name() + ',' + str(vertex[1]) + ')'
            if i != (len(self.adjacentVertices) - 1):
                dispStr += ' - '
        return dispStr

    def get_heuristic_dist(self) -> int:
        return self.heuristic_dist

    def get_edge_weight(self, vertex) -> int:
        for v in self.adjacentVertices:
            if(vertex == v[0]):
                return v[1]
        if(vertex == self):
            return 0
        return -1

# driver code
# v = Vertex(1, "A")
# e = Vertex(2, "E")
# v.set_adjacent_vertices((e,55))
# print(v.get_edge_weight(e))
# print(v.get_name())
