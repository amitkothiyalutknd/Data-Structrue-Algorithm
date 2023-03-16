import numpy as ny
class AdjNode:
    def __init__(self, vertices):
        self.vertex = vertices
        self.next = None

class UndirectGraph:
    def __init__(self, vertices, edges):
        self.vertice = vertices
        self.udgraph = [None] * self.vertice
        self.vertice = [[] for _ in range (vertices)]
        for v1, v2 in edges:
            self.vertice[v1].append(v2)
            self.vertice[v2].append(v1)
    
    def addEdge(self, origin, destination):
        node = AdjNode(destination)
        node.next = self.udgraph[origin]
        self.udgraph[origin] = node

        node = AdjNode(origin)
        node.next = self.udgraph[destination]
        self.udgraph[destination] = node

    def adjacencyList(self):
        print("\n----------------------------Adjacency List of UndirectGraph----------------------------")
        for i in range(len(self.vertice)):
            print("Vertex " + str(i) + ":", end="")
            temp = self.udgraph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
                print(end="")
            print("\n")

    def adjacencyMatrix(self, vertices, edges):
        adjMatrix = ny.zeros(shape = (vertices, vertices))
        for v1, v2 in edges:
            adjMatrix[v1][v2] = 1
            adjMatrix[v2][v1] = 1
        return adjMatrix

    def bFS(self, UndirectGraph, source):
        visited = [False] * len(UndirectGraph.vertice)
        bfslist = [source]
        visited[source] = True
        parent = [None]
        i = 0
        while i < len(bfslist):
            current = bfslist[i]
            visited[current] = True
            for v in UndirectGraph.vertice[current]:
                if not visited[v]:
                    bfslist.append(v)
                    visited[v] = True       
                    parent.append(current)
            i += 1
        print("----------------------------Breadth First Search Representation of UndirectGraph----------------------------")
        output = "BFS Path Representation:\t" + str(bfslist) + "\nParent Nodes Of Each visited vertex in BFS:\t" + str(parent)
        print(output)

    def dFS(self, UndirectGraph, source):
        stack = [source]
        visited = [False] * len(UndirectGraph.vertice)
        dfslist = []
        while len(stack) > 0:
            current = stack.pop()
            if not visited[current]:
                dfslist.append(current)
            visited[current] = True
            for v in UndirectGraph.vertice[current]:
                if not visited[v]:
                    stack.append(v)
        print("\n----------------------------Depth First Search Representation of UndirectGraph----------------------------", )
        output = "DFS Path Reprsentation:\t" + str(dfslist)
        print(output)

vertices = 5
edges = [(0, 1,), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 0)]
udgraph = UndirectGraph(vertices, edges)
print("----------------------------Connected Paired Nodes of UndirectGraph----------------------------\n", udgraph.vertice)
for origin, destination in edges:
    udgraph.addEdge(origin, destination)
udgraph.adjacencyList()
print("\n----------------------------Adjacency Matrix of UndirectGraph----------------------------\n", udgraph.adjacencyMatrix(vertices, edges))
try:
    source = int(input("\nEnter The Source Node:\t"))
    if source > 4:
        print("The UndirectGraph Has Only 5 vertices from 0 to 4.")
    else:
        udgraph.bFS(udgraph, source)
        udgraph.dFS(udgraph, source)
except Exception as error:
            print(f"{error}. Kindly! Choose Correct Number From The Above Mentioned Operation List.")