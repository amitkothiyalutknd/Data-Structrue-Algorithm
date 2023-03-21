import sys
import numpy as ny

class AdjNode:
    def __init__(self, noOfVertices):
        self.vertex = noOfVertices
        self.next = None

class UndirectGraph():
    def __init__(self, noOfVertices):
        self.vertex = noOfVertices
        self.graph = [None] * self.vertex
        self.vertex = [[] for _ in range (noOfVertices)]
    
    def adjacencyList(self, isDirected):
        if isDirected == True:
            print("\n__________________________________________Adjacency List of Directed Weighted Graph__________________________________________")
        else:
            print("\n__________________________________________Adjacency List of Undirected Weighted Graph__________________________________________")
        for i in range(len(self.vertex)):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
                print(end="")
            print("\n")
    
    def UdadjacencyMatrix(self, noOfVertices):
        adjMatrix = ny.zeros(shape = (noOfVertices, noOfVertices))
        for vertex1, vertex2, weight in self.edges:
            adjMatrix[vertex1][vertex2] = weight
            adjMatrix[vertex2][vertex1] = weight
        return adjMatrix

    def UdaddEdge(self, origin, destination):
        node = AdjNode(destination)
        node.next = self.graph[origin]
        self.graph[origin] = node
        node = AdjNode(origin)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def createGraph(self, noOfVertices, noOfEdges, isDirected):
        # self.edges = [(0, 1, 2), (0, 2, 6), (1, 3, 5), (2, 3, 8), (3, 4, 10), (3, 5, 15), (4, 5, 6), (4, 6, 2), (5, 6, 6)] //input for undirected graph 
        # self.edges = [(0, 1, 5), (1, 2, 9), (1, 3, 11), (1, 4, 3), (2, 3, 14), (3, 4, 7), (4, 0, 2)] ////input for directed graph
        while True:
            try:
                self.edges = []
                for index in range(noOfEdges):
                    vertex1, vertex2, weight = list(map(int, input(f"{index + 1}> Enter The Vertex1, Vertex2 and Their Edge Weight Respectively. Seperate Each Input From Single Space Only:\t").split(' ')))
                    self.edges.append((vertex1, vertex2, weight))
            except Exception as error:
                print(f"{error}. Kindly! Enter The Vertices And Weight Of Edge Once Again Carefully.\n")
                pass
            else:
                break
        if isDirected == True:
            print(f"\nTotal Number of Vertices & Edges of Directed Weighted Graph Are {noOfVertices} & {noOfEdges}.")
        elif isDirected == False:
            print(f"\nTotal Number of Vertices & Edges of Undirected Weighted Graph Are {noOfVertices} & {noOfEdges}.")
        v1, v2, w = [i[0] for i in self.edges], [i[1] for i in self.edges], [i[2] for i in self.edges]
        for edge, (start, end, weight) in enumerate(zip(v1, v2, w)):
            print(f"The Weight of Edge:{edge + 1} Between Vertex:{start} and vertex:{end} is {weight}.")
    
    def dijkstra(self, weightedadjMatrix, source):
        self.noParent = -1
        noOfVertices = len(weightedadjMatrix[0])
        shortestDistances = [sys.maxsize] * noOfVertices
        added = [False] * noOfVertices
        for vertexIndex in range(noOfVertices):
            shortestDistances[vertexIndex] = sys.maxsize
            added[vertexIndex] = False
        shortestDistances[source] = 0
        parents = [-1] * noOfVertices
        parents[source] = self.noParent
        for _ in range(1, noOfVertices):
            nearestVertex = -1
            shortestDistance = sys.maxsize
            for vertexIndex in range(noOfVertices):
                if not added[vertexIndex] and shortestDistances[vertexIndex] < shortestDistance:
                    nearestVertex = vertexIndex
                    shortestDistance = shortestDistances[vertexIndex]
            added[nearestVertex] = True
            for vertexIndex in range(noOfVertices):
                edgeDistance = weightedadjMatrix[nearestVertex][vertexIndex]
                if edgeDistance > 0 and shortestDistance + edgeDistance < shortestDistances[vertexIndex]:
                    parents[vertexIndex] = nearestVertex
                    shortestDistances[vertexIndex] = shortestDistance + edgeDistance
        self.printSolution(source, shortestDistances, parents)

    def printSolution(self, source, distances, parents):
        noOfVertices = len(distances)
        print("\nVertex\t\tDistance\t\tPath", end="")
        for vertexIndex in range(noOfVertices):
            if vertexIndex != source:
                print("\n",source, "->", vertexIndex, "\t", distances[vertexIndex], "\t\t\t", end="")
                self.printPath(vertexIndex, parents)
    
    def printPath(self, currentVertex, parents):
        if currentVertex == self.noParent:
            return
        self.printPath(parents[currentVertex], parents)
        print(currentVertex, end=" ")

class DirectedGraph(UndirectGraph):
    def __init__(self, noOfVertices):
        self.vertex = noOfVertices
        self.graph = [None] * self.vertex
        self.vertex = [[] for _ in range (noOfVertices)]
    
    def DadjacencyMatrix(self, noOfVertices):
        adjMatrix = ny.zeros(shape = (noOfVertices, noOfVertices))
        for vertex1, vertex2, weight in self.edges:
            adjMatrix[vertex1][vertex2] = weight
        return adjMatrix

    def DaddEdge(self, origin, destination):
        node = AdjNode(destination)
        node.next = self.graph[origin]
        self.graph[origin] = node

if __name__ == "__main__":
    global noOfVertices
    global noOfEdges
    isDirected = input('Is Graph Directed? (Yes/No): ').lower().strip() == 'yes'
    while True:
        try:
            noOfVertices, noOfEdges = map(int, input("\nEnter The Total Number of Vertices & Edges of Weighted Graph. Seperate Each Input From Single Space Only:").split(" "))
        except Exception as error:
            print(f"{error}. Kindly! Enter The Total Number of Vertices & Edges of Weighted Graph Once Again Carefully.\n")
            pass
        else:
            break    
    if isDirected == False:
        graph = UndirectGraph(noOfVertices)
        graph.createGraph(noOfVertices, noOfEdges, isDirected)
        for origin, destination, weight in graph.edges:
            graph.UdaddEdge(origin, destination)
        print("\n__________________________________________Adjacency Matrix Of Undirected Weighted Graph__________________________________________\n", graph.UdadjacencyMatrix(noOfVertices))
        graph.adjacencyList(isDirected)
        while True:
            try:
                source = eval(input(f"\nChoose The Source Vertex from 0 To {noOfVertices - 1} Find Out The Shortest Path Between Rest Of Nodes Of Undirected Weighted Graph:\t"))
            except Exception as error:
                print(f"{error}. Kindly! Choose The Source Node Value from 0 to {noOfVertices - 1} of Undirected Weighted Graph Once Again Carefully.\n")
            else:
                break
        weightedadjMatrix = graph.UdadjacencyMatrix(noOfVertices)
        graph.dijkstra(weightedadjMatrix, source)
    elif isDirected == True:
        graph = DirectedGraph(noOfVertices)
        graph.createGraph(noOfVertices, noOfEdges, isDirected)
        for origin, destination, weight in graph.edges:
            graph.DaddEdge(origin, destination)
        print("\n__________________________________________Adjacency Matrix Of Directed Weighted Graph__________________________________________\n", graph.DadjacencyMatrix(noOfVertices))
        graph.adjacencyList(isDirected)
        while True:
            try:
                source = eval(input(f"\nChoose The Source Vertex from 0 To {noOfVertices - 1} Find Out The Shortest Path Between Rest Of Nodes Of Directed Weighted Graph:\t"))
            except Exception as error:
                print(f"{error}. Kindly! Choose The Source Node Value from 0 to {noOfVertices - 1} of Directed Weighted Graph Once Again Carefully.\n")
            else:
                break
        weightedadjMatrix = graph.DadjacencyMatrix(noOfVertices)
        graph.dijkstra(weightedadjMatrix, source)