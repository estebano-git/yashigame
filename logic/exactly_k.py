import itertools
from pysat.formula import WCNF


def exactly_k(literals, k):
    """k is the cardinality of literals in the clause, we want it to be = number of points - 1
  as this will result in a spanning tree"""
    wcnf = WCNF()
    cnf = []
    n = len(literals)

    # Exactly k propositional vairables in X are true can be rephrased as the conjunction
    # of at least k and at most k

    # At least k propositional variables
    for combination in itertools.combinations(literals, n - k + 1):
        cnf.append([lit for lit in combination])

    # At most k
    for combination in itertools.combinations(literals, k + 1):
        cnf.append([-lit for lit in combination])

    for clause in cnf:
        wcnf.append(clause)

    return wcnf
