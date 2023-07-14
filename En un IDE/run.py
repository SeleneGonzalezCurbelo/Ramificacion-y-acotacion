import search

# Search methods

ab = search.GPSProblem('A', 'B', search.romania)
bo = search.GPSProblem('B', 'O', search.romania)
st = search.GPSProblem('S', 'T', search.romania)
uv = search.GPSProblem('U', 'V', search.romania)

print("A-B")
print(search.branch_and_bound_graph_search(ab).path())
print(search.branch_and_bound_search_heuristic(ab).path())
print()
print("B-O")
print(search.branch_and_bound_graph_search(bo).path())
print(search.branch_and_bound_search_heuristic(bo).path())
print()
print("S-T")
print(search.branch_and_bound_graph_search(st).path())
print(search.branch_and_bound_search_heuristic(st).path())
print()
print("U-V")
print(search.branch_and_bound_graph_search(uv).path())
print(search.branch_and_bound_search_heuristic(uv).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450