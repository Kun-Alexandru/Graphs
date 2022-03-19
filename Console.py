from DirectedGraph import DirectedGraph
from randomGen import *


class Console():

    def __init__(self, fileName):
        self.__fileName = fileName
        self.__commands = {"0": self.__loadFromFile, "1": self.__getNumberOfVertices,
                           "2": self.__printAllVertices, "3": self.__edgeFromXToY,
                           "4": self.__getDegrees, "6": self.__modifyCost,
                           "7": self.__addVertex, "8": self.__addEdge,
                           "9": self.__removeVertex, "10": self.__removeEdge,
                           "11": self.__copyGraph, "12": self.__printGraph, "13": self.__printGraphCopy,
                           "5": self.__parseOut,"15": self.__isolatedVertices, "14": self.__generateRandom}

    def print(self):
        print("Options:\n")
        print("Type 0 to load the graph from file")
        print("-" * 40)
        print("Type 1 to get the number of vertices")
        print("Type 2 to see all vertices")
        print("Type 3 to see if there is an edge from <x> to <y>")
        print("Type 4 to print the out degree and in degree of a vertex")
        print("Type 5 to see all the edges from a given vertex")
        print("-" * 40)
        print("Graph modifiers:")
        print("Type 6 to modify the cost of an edge")
        print("Type 7 to add a vertex")
        print("Type 8 to add an edge")
        print("Type 9 to remove a vertex")
        print("Type 10 to remove an edge")
        print("-" * 40)
        print("Type 11 to make a copy of the graph. The copy will be stored in the main class as a property.")
        print("Type 12 to print the graph vertices and edges.")
        print("Type 13 to print the copy of the graph with its vertices and edges.")
        print("Type 14 to generate a new graph with number of vertices and edges given")
        print("Type end to exit the program\n\n")

    def __loadFromFile(self):
        try:
            with open(self.__fileName, "r") as file:
                firstLine = file.readline()
                firstLine = firstLine.strip().split()
                vertices, edges = int(firstLine[0]), int(firstLine[1])
                self.__graph = DirectedGraph(vertices)
                for times in range(edges):
                    line = file.readline()
                    line = line.strip().split()
                    start, end, cost = int(line[0]), int(line[1]), int(line[2])
                    self.__graph.addEdge(start, end, cost)
            print("Graph loaded.")
        except IOError:
            raise graphException("File Reading Error")

    def __getNumberOfVertices(self):
        print(self.__graph.getNumberOfVertices())

    def __printAllVertices(self):
        print(self.__graph.parseKeys())

    def __edgeFromXToY(self):
        print("Give vertices x and y:")
        start = int(input())
        end = int(input())
        result = {True: "Yes", False: "No"}
        print(result[self.__graph.isEdge(start, end)])

    def __getDegrees(self):
        print("Give vertex:")
        vertex = int(input())
        print("Out degree: " + str(self.__graph.getOutDegree(vertex)))
        print("In degree: " + str(self.__graph.getInDegree(vertex)))

    def __modifyCost(self):
        print("Give edge start:")
        start = int(input())
        print("Give edge end:")
        end = int(input())
        print(self.__graph.retrieveCost(start, end))
        print("Give new cost:")
        cost = int(input())
        self.__graph.modifyEdgeCost(start, end, cost)

    def __addVertex(self):
        print("Give new vertex:")
        vertex = int(input())
        self.__graph.addVertex(vertex)

    def __isolatedVertices(self):
        print(self.__graph.allIsolatedVertices())

    def __parseOut(self):
        print("Get vertex:")
        x = int(input())
        print("The OUT edges from the given vertex are :", end =" ")
        out = self.__graph.parseIterableOut(x)
        print(out)
        print("The IN edges from the given vertex are : ", end =" ")
        inZ = self.__graph.parseIterableIn(x)
        print(inZ)

    def __addEdge(self):
        print("Give edge start: ")
        start = int(input())
        print("Give edge end: ")
        end = int(input())
        print("Give edge cost: ")
        cost = int(input())
        self.__graph.addEdge(start, end, cost)

    def __removeEdge(self):
        print("Give edge start:")
        start = int(input())
        print("Give edge end:")
        end = int(input())
        self.__graph.removeEdge(start, end)

    def __generateRandom(self):

        numberOfVertices = int(input("Give me the number of vertices"))
        numberOfEdges = int(input("Give me the number of edges"))
        g = RandomGraphGenerator(numberOfVertices,numberOfEdges)
        self.__graph = g.get_graph()
        g.printGraph()

    def __removeVertex(self):
        print("Give vertex you want to remove:")
        vertex = int(input())
        self.__graph.removeVertex(vertex)

    def __copyGraph(self):
        print("Copying the graph...")
        self.__graphCopy = self.__graph.copyGraph()
        print("The graph is now copied and stored in __graphCopy")

    def __printGraphCopy(self):
        print(self.__graphCopy.parseKeys())
        print(self.__graphCopy.edges())

    def __printGraph(self):
        print("The vertices of the graph are: ")
        print(self.__graph.parseKeys())
        print("The edges of the graph are: ")
        print(self.__graph.edges())

    def run(self):
        while True:
            self.print()
            print(">>")
            cmd = input()
            if cmd == "end":
                return
            elif cmd in self.__commands:
                try:
                    self.__commands[cmd]()
                except graphException as e:
                    print(e)
            else:
                print("Wrong cmd")

c = Console("graph10.txt")
c.run()