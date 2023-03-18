import numpy as ny
class AdjNode:
    def __init__(self, vertices):
        self.vertex = vertices
        self.next = None
        
class DirectedGraph:
    def __init__(self, vertices, edges):
        self.vertice = vertices
        self.dgraph = [None] * self.vertice
        self.vertice = [[] for _ in range (vertices)]
        for v1, v2 in edges:
            self.vertice[v1].append(v2)
    
    def addEdge(self, origin, destination):
        node = AdjNode(destination)
        node.next = self.dgraph[origin]
        self.dgraph[origin] = node

    def adjacencyList(self):
        print("\n----------------------------Adjacency List of DirectedGraph----------------------------")
        for i in range(len(self.vertice)):
            print("Vertex " + str(i) + ":", end="")
            temp = self.dgraph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
                print(end="")
            print("\n")

    def adjacencyMatrix(self, vertices, edges):
        adjMatrix = ny.zeros(shape = (vertices, vertices))
        for v1, v2 in edges:
            adjMatrix[v1][v2] = 1
        return adjMatrix

    def bFS(self, DirectedGraph, source):
        visited = [False] * len(DirectedGraph.vertice)
        bfslist = [source]
        visited[source] = True
        parent = [None]
        i = 0
        while i < len(bfslist):
            current = bfslist[i]
            visited[current] = True
            for v in DirectedGraph.vertice[current]:
                if not visited[v]:
                    bfslist.append(v)
                    visited[v] = True       
                    parent.append(current)
            i += 1
        print("----------------------------Breadth First Search Representation of DirectedGraph----------------------------")
        output = "BFS Path Representation:\t" + str(bfslist) + "\nParent Nodes Of Each visited vertex in BFS:\t" + str(parent)
        print(output)

    def dFS(self, DirectedGraph, source):
        stack = [source]
        visited = [False] * len(DirectedGraph.vertice)
        dfslist = []
        while len(stack) > 0:
            current = stack.pop()
            if not visited[current]:
                dfslist.append(current)
            visited[current] = True
            for v in DirectedGraph.vertice[current]:
                if not visited[v]:
                    stack.append(v)
        print("\n----------------------------Depth First Search Representation of UndirectGraph----------------------------", )
        output = "DFS Path Reprsentation:\t" + str(dfslist)
        print(output)

vertices = 6
edges = [(0, 1,), (0, 2), (0, 3), (1, 2), (3, 4), (3, 5), (4, 0), (4, 2) ]
dgraph = DirectedGraph(vertices, edges)
print("----------------------------Connected Paired Nodes of DirectedGraph----------------------------\n", dgraph.vertice)
for origin, destination in edges:
    dgraph.addEdge(origin, destination)
dgraph.adjacencyList()
print("\n----------------------------Adjacency Matrix of DirectedGraph----------------------------\n", dgraph.adjacencyMatrix(vertices, edges))
try:
    source = int(input("\nEnter The Source Node:\t"))
    if source > 5:
        print("The DirectedGraph Has Only 6 vertices from 0 to 5.")
    else:
        dgraph.bFS(dgraph, source)
        dgraph.dFS(dgraph, source)
except Exception as error:
            print(f"{error}. Kindly! Choose Correct Number From The Above Mentioned Operation List.")