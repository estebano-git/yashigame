from logic.no_crossings import no_crossings
from init_game import get_points, generate_edges
from logic.no_cycles import no_cycles
from logic.exactly_k import exactly_k
from logic.all_constraints import constraints
from logic.soft_constraints import wcnf_edges

points = get_points(5, 10, 0)
literals, edges, weights = generate_edges(points)
cross_cnf = no_crossings(literals, edges)
print(cross_cnf.hard)
cycles_cnf = no_cycles(points, literals, edges, weights)
print(cycles_cnf.hard)
k = len(points) - 1
exactly_k_cnf = exactly_k(literals, k)
print(exactly_k_cnf.hard)

all_cnfs = constraints(points, literals, edges, weights)
print(all_cnfs.hard)

wcnf_edges = wcnf_edges(literals, weights)
print(wcnf_edges.soft)
print(wcnf_edges.wght)