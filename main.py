import networkx as nx
from init_game import generate_points, get_points, generate_edges
from logic.all_constraints import constraints
from plot_graph import plot_graph
from pysat.examples.fm import FM
from pysat.solvers import Solver
from graph import create_graph
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Yashi Game')

    parser.add_argument('--grid-size', type=int, default=5, help='Size of the grid')
    parser.add_argument('--sat-mode', choices=['sat', 'maxsat'], default='maxsat', help='SAT mode: sat or maxsat')
    parser.add_argument('--points-mode', choices=['random', 'file'], default='random', help='Points generation mode')
    parser.add_argument('--file-path', type=str, help='Path to the points file')
    parser.add_argument('--num-points', type=int, default=10, help='Number of points for random generation')
    parser.add_argument('--seed', type=int, default=0, help='Random seed')

    return parser.parse_args()


def yashi_game(args):
    grid_size = args.grid_size
    sat_mode = args.sat_mode
    points_mode = args.points_mode
    file_path = args.file_path
    num_points = args.num_points
    seed = args.seed

    if points_mode == 'random':
        points = generate_points(grid_size, num_points, seed)
    else:
        points = get_points(file_path=file_path)

    literals, edges, weights, lits_edges_dict = generate_edges(points)

    plot_graph(grid_size, points, title='The game')

    wcnf = constraints(points, literals, edges, weights)

    # SAT solver
    if sat_mode == 'sat':
        solver = Solver(name='Minisat22')
        solver.append_formula(wcnf.hard)
        if solver.solve():
            sat_model = solver.get_model()
            model_edges = [lits_edges_dict[x] for x in sat_model if x > 0]
            graph = create_graph(points, model_edges, weights)
            # Check that our graph is connected, if not there is no solution
            if not nx.is_connected(graph):
                print('No solution')
                return
            print('Game is solvable')
            plot_graph(grid_size, points, model_edges, 'Solution')
        else:
            print('No solution')
    # MaxSAT solver
    else:
        solver = FM(wcnf, verbose=0)
        if solver.compute():
            sat_model = solver.model
            model_edges = [lits_edges_dict[x] for x in sat_model if x > 0]
            graph = create_graph(points, model_edges, weights)
            if not nx.is_connected(graph):
                print('No solution')
                return
            print('Game is solvable')
            plot_graph(grid_size, points, model_edges, 'Optimal Solution')
        else:
            print('No solution')


if __name__ == "__main__":
    arguments = parse_args()
    yashi_game(arguments)
