""" This module contains tests for the search.graph.py module. It
tests both Vertex and Graph classes."""

import pytest
from search import Vertex

# tests for Vertex class
@pytest.fixture
def vertex():
    """Returns a Vertex instance named 'v1'."""
    return Vertex('v1')

def test_setting_vertex_name(vertex):
    assert vertex.name == 'v1'

def test_default_vertex_distance(vertex):
    assert vertex._distance == 99999

def test_default_vertex_colour(vertex):
    assert vertex._colour == 'black'





