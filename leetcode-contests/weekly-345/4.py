# 2685. Count the Number of Complete Components
class Solution:
  def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    """
    union find, but also keep track of edges
    for each component of size c
      if the number of edges equals (c * (c - 1)) // 2, it is fully connected
    """
    parent = [n for n in range(n)]
    size = [1 for _ in range(n)]
    num_edges = [0 for _ in range(n)]

    def root(node):
      if parent[node] == node:
        return node
      result = root(parent[node])
      parent[node] = result
      return result

    def union(x, y):
      r1, r2 = root(x), root(y)
      if r1 == r2:
        num_edges[r1] += 1
        return
      if size[r1] < size[r2]:
        r1, r2 = r2, r1
      parent[r2] = parent[r1]
      size[r1] += size[r2]
      num_edges[r1] += num_edges[r2]
      num_edges[r1] += 1

    for a, b in edges:
      union(a, b)

    result = 0
    seen = set()
    for component in parent:
      r = root(component)
      if r not in seen:
        seen.add(r)
        c = size[r]
        if (c * (c - 1)) // 2 == num_edges[r]:
          result += 1

    return result
