from pysat.formula import WCNF
from logic.exactly_k import exactly_k
from logic.no_cycles import no_cycles
from logic.no_crossings import no_crossings
from logic.edges_weights import wcnf_edges


def constraints(points, literals, edges, weights):
    wcnf = WCNF()
    k = len(points) - 1

    wcnf_exactly_k = exactly_k(literals, k)
    wcnf_no_crossings = no_crossings(literals, edges)
    wcnf_no_cycles = no_cycles(points, literals, edges, weights)
    wcnf_edges_soft = wcnf_edges(literals, weights)

    wcnf.extend(wcnf_exactly_k.hard)
    wcnf.extend(wcnf_no_crossings.hard)
    wcnf.extend(wcnf_no_cycles.hard)
    wcnf.extend(wcnf_edges_soft.soft, weights=wcnf_edges_soft.wght)

    return wcnf
