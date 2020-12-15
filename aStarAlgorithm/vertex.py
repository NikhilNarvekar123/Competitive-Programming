
class Vertex:

    def __init__(self, value, name="node"):
        self.value = value
        self.name = name
        self.adjacentVertices = []

    def setAdjacentVertices(self, *args):
        for arg in args:
            self.adjacentVertices.append(arg)

    def getValue(self) -> int:
        return self.value

    def getName(self) -> str:
        return self.name

    def getAdjacentVertices(self) -> list:
        return self.adjacentVertices

    def display_adjacent_vertices(self) -> str:
        dispStr = ''
        for i in range(len(self.adjacentVertices)):
            vertex = self.adjacentVertices[i]
            dispStr += '(' + vertex[0].getName() + ',' + str(vertex[1]) + ')'
            if i != (len(self.adjacentVertices) - 1):
                dispStr += ' - '
        return dispStr


    def getEdgeWeight(self, vertex) -> int:
        for v in self.adjacentVertices:
            if(vertex == v[0]):
                return v[1]
        return -1

# driver code
# v = Vertex(1, "A")
# e = Vertex(2, "E")
# v.setAdjacentVertices((e,55))
# print(v.getEdgeWeight(e))
# print(v.getName())
