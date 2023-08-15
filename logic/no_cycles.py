import networkx as nx
from pysat.formula import WCNF
from graph import add_edges_graph
from init_game import generate_edges


# Use the cycles subgraphs from nx to get the edges we would need to cut
def no_cycles(points, literals, edges, weights) -> WCNF:
    """ Inputs the points, edges and weights
  Output the CNFS with the edges that must be cut to break each subcycle"""
    wcnf = WCNF()
    # Generate our graph
    graph = nx.Graph()
    graph.add_nodes_from(points)
    graph = add_edges_graph(graph, edges, weights)

    # Get all subcycles from the graph, each subcycle is a list of nodes
    cycles = nx.cycle_basis(graph, root=None)

    # Get all edges that are part of the subcycles
    edges_cycles = []
    for cycle in cycles:
        edges_cycles.append(generate_edges(cycle)[1])

    # Map our edges to literals (in original edges)
    cnf = []
    for cycle in edges_cycles:
        # print(cycle)
        clause = []
        for edge in cycle:
            # print(edge)
            edge_index = edges.index(edge)
            literal = literals[edge_index]
            clause.append(-literal)
        cnf.append(clause)

    for clause in cnf:
        wcnf.append(clause)

    return wcnf
