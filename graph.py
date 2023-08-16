import networkx as nx


def create_graph(points, edges=[], weights=[]): # See if we delete this
    """Input a list of points outputs a graph with edges"""
    graph = nx.Graph()
    graph.add_nodes_from(points)
    if len(edges) > 0 and len(weights):
        for index, edge in enumerate(edges):
            graph.add_edge(edge[0], edge[1], weight=weights[index])
    elif len(edges) > 0:
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
    return graph


def add_edges_graph(graph, edges, weights):

    graph = graph.copy()
    for index, edge in enumerate(edges):
        graph.add_edge(edge[0], edge[1], weight=weights[index])

    return graph


def get_edges_dict(edges):
    """Input edges returns dictionary mapping to natural numbers {edge:integer}"""

    mapping = {}
    i = 1

    for edge in edges:
        mapping[edge] = i
        i = i + 1

    return mapping
