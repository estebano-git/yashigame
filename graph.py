import networkx as nx


def create_graph_no_edges(points):

    g = nx.Graph()
    g.add_nodes_from(points)
    edges = list(nx.minimum_spanning_edges(g, algorithm='kruskal'))
    print(edges)
    g.add_edges_from(edges)
    print(g)

    return g


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
