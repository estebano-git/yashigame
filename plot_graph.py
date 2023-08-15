import matplotlib as plt
import networkx as nx


def plot_graph(grid_size, points, graph, title=""):
    plt.figure(figsize=(grid_size, grid_size))
    pos = dict((point, point) for point in points)

    for row in range(grid_size):
        for col in range(grid_size):
            plt.plot(col, row, 'ko')  # Black point for empty cells

    nx.draw(graph, pos, with_labels=True, node_size=200, font_size=10, font_color='black')
    plt.title(title)
    plt.show()
