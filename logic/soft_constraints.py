from pysat.formula import WCNF


def wcnf_edges(literals, weights):
    """Returns the WCNF object with the negative of the edge length as weight
    for MaxSat solving"""
    wcnf = WCNF()
    for index, literal in enumerate(literals):
        print(literal)
        wcnf.append([literal], weight=-weights[index])

    return wcnf
