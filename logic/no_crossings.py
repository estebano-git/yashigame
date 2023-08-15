from pysat.formula import WCNF

def no_crossings(literals, edges) -> WCNF:
  """Input the list of edges
  Returns a list of tuples of those edges that cross each other"""
  wcnf = WCNF()
  cnf_crossings = set()

  for index1, edge1 in enumerate(edges):
    edge1_point1 = edge1[0]
    edge1_point2 = edge1[1]
    for index2, edge2 in enumerate(edges):
      edge2_point1 = edge2[0]
      edge2_point2 = edge2[1]
      if (edge1 != edge2 and edge1_point1[0] < edge2_point2[0] < edge1_point2[0]
          and edge2_point2[1] > edge1_point1[1] > edge2_point1[1]):
        cnf_crossings.add((literals[index1], literals[index2]))

  for clause in cnf_crossings:
    wcnf.append(list(-literal for literal in clause))

  return wcnf