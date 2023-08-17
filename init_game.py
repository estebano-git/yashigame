import random
import pandas as pd


def generate_points(grid_size, num_points, seed):
    random.seed(seed)
    """Return the list of points"""

    if num_points > grid_size * grid_size:
        raise ValueError("Number of points cannot exceed grid size.")

    # Generate random points without overlapping:
    points = set()
    while len(points) < num_points:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        points.add((x, y))
    return list(points)


def get_points(file_path: str):
    """Input file path
    Return list of tuples (points)"""
    df = pd.read_csv(file_path, header=None)
    points = [tuple(row) for row in df.values]
    return points


def generate_edges(points):
    """Returns lists: literals, edges, weights and lits_edges_dict mapping"""
    # Our literals are mapped to the natural numbers
    i = 1

    literals = []
    edges = []
    weights = []
    lits_edges_dict = {}

    # Sort the points ascending, for vertical edges
    points_vert = sorted(points, key=lambda x: (x[0], x[1]))
    # Sort the points ascending but by the 1 value for horizontal edges
    points_hor = sorted(points, key=lambda x: (x[1], x[0]))

    # Get the vertical edges
    for index, point in enumerate(points_vert):
        if index < len(points_vert) - 1 and point[0] == points_vert[index + 1][0]:
            literals.append(i)
            edge = (point, points_vert[index + 1])
            edges.append(edge)
            weights.append(points_vert[index + 1][1] - point[1])
            lits_edges_dict[i] = edge
            i = i + 1

    # Get the horizontal edges
    for index, point in enumerate(points_hor):
        if index < len(points_hor) - 1 and point[1] == points_hor[index + 1][1]:
            literals.append(i)
            edge = (point, points_hor[index + 1])
            edges.append(edge)
            weights.append(points_hor[index + 1][0] - point[0])
            lits_edges_dict[i] = edge
            i = i + 1

    return literals, edges, weights, lits_edges_dict
