"""
This module contains classes that are needed to represent
directed and undirected graphs.
"""

BLACK = 'black'

class Vertex(object):
    """ Provides the data structure for the vertex of a graph."""

    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self._distance = 99999
        self._colour = BLACK

    def add_neighbours(self, neighbours):
        """
        Adds one or more neighbour vertices to a vertex
        """
        for neighbour in neighbours:
            # check that neighbour doesn't exist already
            if neighbour not in self.neighbours:
                self.neighbours.append()
                self.neighbours.sort()

    def remove_neighbours(self, neighbours):
        """
        Removes one or more neighbour vertices from a vertex
        """
        for neighbour in neighbours:
            # check that neighbour exists
            if neighbour in self.neighbours:
                self.neighbours.remove(neighbour)
                self.neighbours.sort()



class Graph(object):

    def __init__(self, vertices=[]):
        pass
