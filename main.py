

from logic.no_crossings import no_crossings
from init_game import get_points, generate_edges
from logic.no_cycles import no_cycles
from logic.exactly_k import exactly_k
from logic.all_constraints import constraints
from logic.edges_weights import wcnf_edges
from plot_graph import plot_graph
from pysat.formula import WCNF
from pysat.examples.fm import FM
from graph import add_edges_graph
import networkx as nx
from pysat.solvers import Solver, Minisat22


grid_size = 5
num_points = 10
points = get_points(grid_size, num_points, seed=0)
#plot_graph(grid_size, points, title='Game')

literals, edges, weights, lits_edges_dict = generate_edges(points)
for index, edge in enumerate(edges):
    print(f'{literals[index]}')
    print(f'{edge=}')


graph = nx.Graph()
graph.add_nodes_from(points)
graph = add_edges_graph(graph, edges, weights)
cycles = nx.cycle_basis(graph, root=None)
print(f'{cycles=}')


print(f'{cycles=}')

cross_cnf = no_crossings(literals, edges)
print(cross_cnf.hard) # This seems correct
cycles_cnf = no_cycles(points, literals, edges, weights)


print(cycles_cnf.hard) # Identified correctly two cycles,
print('Cycles CNF hard')

k = len(points) - 1
exactly_k_cnf = exactly_k(literals, k)
print(exactly_k_cnf.hard)

all_cnfs = constraints(points, literals, edges, weights)
print(all_cnfs.hard)

wcnf_edges = wcnf_edges(literals, weights)
print(wcnf_edges.soft)
print(wcnf_edges.wght)

wcnf = WCNF()
wcnf.extend(all_cnfs.hard)
wcnf.extend(wcnf_edges.soft, weights=wcnf_edges.wght)
# SAT
solver = Solver(name='Minisat22')
solver.append_formula(wcnf.hard)
print(f'{solver.solve()=}')
sat_model = solver.get_model()
print(f'{sat_model=}')
model_edges = [lits_edges_dict[x] for x in sat_model if x > 0]
plot_graph(grid_size, points, model_edges, 'Solution')


# MaxSat
fm = FM(wcnf, verbose=0)
print(fm.compute())
print(fm.cost)
print(fm.model)
sat_model = fm.model
model_edges = [lits_edges_dict[x] for x in sat_model if x > 0]
plot_graph(grid_size, points, model_edges, 'Optimal Solution')

# Lets wrap it all up

