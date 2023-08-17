import networkx as nx
from pysat.formula import WCNF
from init_game import generate_edges
from graph import create_graph


# Use the cycles subgraphs from nx to get the edges we would need to cut
def no_cycles(points, literals, edges, weights) -> WCNF:
    """ Inputs the points, edges and weights
  Output the CNFS with the edges that must be cut to break each subcycle"""
    wcnf = WCNF()
    # Generate our graph
    graph = create_graph(points, edges, weights)

    # Get cycles basis from the graph, each base cycle is a list of nodes
    cycles = nx.cycle_basis(graph, root=None)

    # Get all edges that are part of the cycles
    edges_cycles = []
    for cycle in cycles:
        edges_cycles.append(generate_edges(cycle)[1])

    # Map edges to -literals
    cnf = []
    for cycle in edges_cycles:
        clause = []
        for edge in cycle:
            edge_index = edges.index(edge)
            literal = literals[edge_index]
            clause.append(-literal)
        cnf.append(clause)

    for clause in cnf:
        wcnf.append(clause)

    return wcnf
