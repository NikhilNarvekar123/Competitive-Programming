from vertex import Vertex
from graph import Graph
from timeit import default_timer as timer
from datetime import timedelta
import math as m


def run_astar(graph : Graph, startVertex: Vertex, endVertex : Vertex):

    startTime = timer()

    vertices = graph.get_vertices()
    visitedVertices = []
    shortestDistances = {}
    totalDistances = {}
    predecessorList = {}

    for vertex in vertices:
        shortestDistances[vertex] = m.inf

    shortestDistances[startVertex] = 0
    totalDistances[startVertex] = shortestDistances[startVertex] + startVertex.get_heuristic_dist()

    while vertices:

        minVal = m.inf
        popIdx = -1
        for i in range(len(vertices)):
            vertex = vertices[i]
            if (vertex in totalDistances) and (totalDistances[vertex] < minVal):
                minVal = totalDistances[vertex]
                popIdx = i

        if popIdx == -1:
            break

        minVertex = vertices.pop(popIdx)

        if minVertex == endVertex:
            break

        visitedVertices.append(minVertex)


        adjacentVertices = minVertex.get_adjacent_vertices()

        for vertex in adjacentVertices:
            if vertex in visitedVertices:
                continue
            dist = shortestDistances[minVertex] + minVertex.get_edge_weight(vertex)
            if dist < shortestDistances[vertex]:
                shortestDistances[vertex] = dist
                totalDistances[vertex] = shortestDistances[vertex] + vertex.get_heuristic_dist()
                predecessorList[vertex] = minVertex

    endTime = timer()
    timeElapsed = timedelta(seconds=endTime-startTime)

    print('For start vertex: ' + startVertex.get_name() + " to end vertex: " + endVertex.get_name(), end="\n")
    print('Shortest Distances')
    for dist in shortestDistances:
        print(dist.get_name() + "->" + str(shortestDistances[dist]))
    print('\nTotal Distances')
    for dist in totalDistances:
        print(dist.get_name() + "->" + str(totalDistances[dist]))
    print('\nPredecessor List')
    for entry in predecessorList:
        print(entry.get_name() + '->' + predecessorList[entry].get_name())
    print('\nPath:')
    pathStr = ''
    lastVertex = endVertex
    while endVertex in predecessorList:
        pathStr = endVertex.get_name() + ' > ' + pathStr if endVertex != lastVertex else endVertex.get_name()
        endVertex = predecessorList[endVertex]
    pathStr = endVertex.get_name() + ' > ' + pathStr
    print(pathStr)
    print('\n')

    return timeElapsed






def run_dijkstra(graph : Graph, startVertex : Vertex):

    startTime = timer()

    vertices = graph.get_vertices()
    shortestDistances = {}
    predecessorList = {}

    for vertex in vertices:
        shortestDistances[vertex] = m.inf

    shortestDistances[startVertex] = 0

    while vertices:

        minVal = m.inf
        popIdx = -1
        for i in range(len(vertices)):
            vertex = vertices[i]
            if shortestDistances[vertex] <= minVal:
                minVal = shortestDistances[vertex]
                popIdx = i


        minVertex = vertices.pop(popIdx)

        if(shortestDistances[minVertex] == m.inf):
            break

        adjacentVertices = minVertex.get_adjacent_vertices()

        for vertex in adjacentVertices:
            dist = shortestDistances[minVertex] + minVertex.get_edge_weight(vertex)
            if dist < shortestDistances[vertex]:
                shortestDistances[vertex] = dist
                predecessorList[vertex] = minVertex


    endTime = timer()
    timeElapsed = timedelta(seconds=endTime-startTime)

    print('For start vertex: ' + startVertex.get_name(), end="\n")
    print('Shortest Distances')
    for dist in shortestDistances:
        print(dist.get_name() + "->" + str(shortestDistances[dist]))
    print('\nPredecessor List')
    for entry in predecessorList:
        print(entry.get_name() + '->' + predecessorList[entry].get_name())
    print('\n')

    return timeElapsed


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

# straight-line heuristic
a.set_heuristic_dist(14)
b.set_heuristic_dist(12)
c.set_heuristic_dist(11)
d.set_heuristic_dist(6)
e.set_heuristic_dist(4)
f.set_heuristic_dist(11)
g.set_heuristic_dist(0)

graph = Graph()
graph.add_vertex(a,b,c,d,e,f,g)

graph.show_graph()
print('\n')

timeTakenDijkstra = run_dijkstra(graph, g)
timeTakenAstar = run_astar(graph, a, g)

print('\nTime Taken:')
print('Dijkstra Method: ', timeTakenDijkstra)
print('A* Method: ', timeTakenAstar)
