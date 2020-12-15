
class Vertex:

    def __init__(self, value, name="node"):
        self.value = value
        self.name = name
        self.adjacentVertices = []

    def set_adjacent_vertices(self, *args):
        for arg in args:
            self.adjacentVertices.append(arg)

    def get_value(self) -> int:
        return self.value

    def get_name(self) -> str:
        return self.name

    def get_adjacent_vertices(self) -> list:
        return self.adjacentVertices

    def display_adjacent_vertices(self) -> str:
        dispStr = ''
        for i in range(len(self.adjacentVertices)):
            vertex = self.adjacentVertices[i]
            dispStr += '(' + vertex[0].get_name() + ',' + str(vertex[1]) + ')'
            if i != (len(self.adjacentVertices) - 1):
                dispStr += ' - '
        return dispStr


    def get_edge_weight(self, vertex) -> int:
        for v in self.adjacentVertices:
            if(vertex == v[0]):
                return v[1]
        return -1

# driver code
# v = Vertex(1, "A")
# e = Vertex(2, "E")
# v.set_adjacent_vertices((e,55))
# print(v.get_edge_weight(e))
# print(v.get_name())
