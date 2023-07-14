# Search methods

ab = GPSProblem('A', 'B', romania)
bo = GPSProblem('B', 'O', romania)
st = GPSProblem('S', 'T', romania)
uv = GPSProblem('U', 'V', romania)

print("A-B")
print(branch_and_bound_graph_search(ab).path())
print(branch_and_bound_search_heuristic(ab).path())
print()
print("B-O")
print(branch_and_bound_graph_search(bo).path())
print(branch_and_bound_search_heuristic(bo).path())
print()
print("S-T")
print(branch_and_bound_graph_search(st).path())
print(branch_and_bound_search_heuristic(st).path())
print()
print("U-V")
print(branch_and_bound_graph_search(uv).path())
print(branch_and_bound_search_heuristic(uv).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450