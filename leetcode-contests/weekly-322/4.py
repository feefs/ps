# 2493. Divide Nodes Into the Maximum Number of Groups
class Solution:
  def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
    """
    compute the connected components of the graph using union find
    for each connected component
      for each node in the connected component
        check if it's bipartite starting from that node with bfs and two-coloring
        the number of groups is the number of levels traversed in bfs
    if any connected component is not bipartite, return -1
    sum the maximum number of groups for each connected component
    """
    # Union Find
    parent = [-1] + [i for i in range(1, n + 1)]
    size = [1] * (n + 1)

    def root(node):
      if parent[node] == node:
        return node
      result = root(parent[node])
      parent[node] = result
      return result

    def union(x, y):
      r1, r2 = root(x), root(y)
      if r1 == r2:
        return
      if size[r1] < size[r2]:
        x, y = y, x
      parent[r2] = parent[r1]
      size[r1] += size[r2]

    # construct the graph and union find to compute the connected components
    graph = defaultdict(lambda: set())
    for a, b in edges:
      union(a, b)
      graph[a].add(b)
      graph[b].add(a)

    # returns how many levels a connected component contains if its bipartite
    # returns -1 otherwise
    def bipartite_bfs(node):
      result = 0
      visited = set()
      q = deque([node])
      color = {node: True}
      expected_child_color = False
      while q:
        q2 = deque([])
        while q:
          curr = q.popleft()
          if curr not in visited:
            visited.add(curr)
            for child in graph[curr]:
              if child in color:
                # if a child is already colored but not what we expect
                # the graph is not two-colorable => not bipartite
                if color[child] != expected_child_color:
                  return -1
              else:
                color[child] = expected_child_color
                q2.append(child)
        q = q2
        expected_child_color = not expected_child_color
        result += 1
      return result

    component_max_groups = defaultdict(lambda: 0)
    for i in range(1, n + 1):
      v = bipartite_bfs(i)
      if v == -1:
        return -1
      r = root(i)
      component_max_groups[r] = max(component_max_groups[r], v)

    return sum(component_max_groups.values())
