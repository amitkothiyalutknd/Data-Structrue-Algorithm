import sys
sys.setrecursionlimit(100000000)

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]
        # return print(self.graphDict)

    def getPaths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return []
        paths = []
        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getPaths(node, end, path)
                for p in newPath:
                    paths.append(p)
        return paths

    def getShortestPath(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return None
        shortestPath = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.getShortestPath(node, end, path)
                if sp:
                    if shortestPath is None or len(sp) > len(shortestPath):
                        shortestPath = sp
        return shortestPath
        
    def inputCities(self):
        try:
            depPort, destPort = (int(value) for value in input('''
            1> Auckland
            2> Brisbane
            3> California
            4> Dehradun
            5> Seattle
            6> Washington

            Select Start & Destination Cities from above list to find out the routes. Seperate Start & Destination Cities from Single Space.''').split(' '))
        
            if depPort == 1:
                start = "Auckland"
            elif depPort == 2:
                start = "Brisbane"
            elif depPort == 3:
                start = "California"
            elif depPort == 4:
                start = "Dehradun"
            elif depPort == 5:
                start = "Seattle"
            else:
                start = "Washington"
            
            if destPort == 1:
                end = "Auckland"
            elif destPort == 2:
                end = "Brisbane"
            elif destPort == 3:
                end = "California"
            elif destPort == 4:
                end = "Dehradun"
            elif destPort == 5:
                end = "Seattle"
            else:
                end = "Washington"
        except Exception as error:
            print(f"{error}. Kindly! Insert Inputs Carefully.")

        print("All The Possible Routes are:\n", self.getPaths(start, end))
        print("\n& The Shortest Route is:\n", self.getShortestPath(start, end))

if __name__ == '__main__':
    routes = {
        ("Dehradun", "Seattle"),
        ("Dehradun", "California"),
        ("Seattle", "California"),
        ("Seattle", "Brisbane"),
        ("Seattle", "Auckland"),
        ("California", "Brisbane"),
        ("California", "Auckland"),
        ("Brisbane", "Auckland"),
        ("Brisbane", "Washington")
    }

    routesGraph = Graph(routes)
    routesGraph.inputCities()