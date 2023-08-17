import networkx as nx


def create_graph(points, edges=[], weights=[]): # See if we delete this
    """Input a list of points outputs a graph with edges"""
    graph = nx.Graph()
    graph.add_nodes_from(points)
    if len(edges) > 0 and len(weights) > 0:
        for index, edge in enumerate(edges):
            graph.add_edge(edge[0], edge[1], weight=weights[index])
    elif len(edges) > 0:
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
    return graph

