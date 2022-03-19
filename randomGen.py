from DirectedGraph import *
from random import *

class RandomGraphGenerator():

    def __init__(self, n, m):

        self.__graph = DirectedGraph(n)
        self.__generate(n, m)

    def __generate(self, n, m):
        setOfVertices = [i for i in range(n)]
        costs = [0]
        for i in range(1, 101):
            costs.append(i)
            costs.append(-i)
        index = 0
        while index < m:
            start = choice(setOfVertices)
            end = choice(setOfVertices)
            cost = choice(costs)
            try:
                self.__graph.addEdge(start, end, cost)
                index += 1
            except graphException:
                pass

    def get_graph(self):
        return self.__graph

    def printGraph(self):
        print("The vertices of the graph are: ")
        print(self.__graph.parseKeys())
        print("The edges of the graph are: ")
        print(self.__graph.edges())
        print("Costs are:")
        print(self.__graph.costs())
