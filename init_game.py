import random
import pandas as pd


def get_points(grid_size, num_points, seed, mode='random', file=''):
    random.seed(seed)
    """Return the list of points"""

    if mode == 'random':
        if num_points > grid_size * grid_size:
            raise ValueError("Number of points cannot exceed grid size.")

        # Get random points without overlapping:
        points = set()
        while len(points) < num_points:
            x = random.randint(0, grid_size - 1)
            y = random.randint(0, grid_size - 1)
            points.add((x, y))

    else:
        assert isinstance(file, str), "Give file path"
        df = pd.read_csv(file, header=None)
        points = [tuple(row) for row in df.values]

    return list(points)


def generate_edges(points):
    """Returns a tuple with lists: literals, edges, weights"""
    # Our literals are mapped to the natural numbers
    i = 1

    literals = []
    edges = []
    weights = []

    # Sort the points ascending, for vertical edges
    points_vert = sorted(points, key=lambda x: (x[0], x[1]))
    # Sort the points ascending but by the 1 value for horizontal edges
    points_hor = sorted(points, key=lambda x: (x[1], x[0]))

    # Get the vertical edges
    for index, point in enumerate(points_vert):
        if index < len(points_vert) - 1 and point[0] == points_vert[index + 1][0]:
            literals.append(i)
            edges.append((point, points_vert[index + 1]))
            weights.append(points_vert[index + 1][1] - point[1])
            i = i + 1

    # Get the horizontal edges
    for index, point in enumerate(points_hor):
        if index < len(points_hor) - 1 and point[1] == points_hor[index + 1][1]:
            literals.append(i)
            edges.append((point, points_hor[index + 1]))
            weights.append(points_hor[index + 1][0] - point[0])
            i = i + 1

    return literals, edges, weights
