# 2477. Minimum Fuel Cost to Report to the Capital
class Solution:
  def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    num_nodes = len(roads) + 1
    graph = defaultdict(lambda: set())
    for i, j in roads:
      graph[i].add(j)
      graph[j].add(i)

    num_reps_leaving = [0 for _ in range(num_nodes)]
    visited = set()

    def dfs(curr):
      if curr in visited:
        return
      visited.add(curr)
      for child in graph[curr]:
        if child not in visited:
          dfs(child)
          num_reps_leaving[curr] += num_reps_leaving[child]
      num_reps_leaving[curr] += 1

    for node in range(num_nodes):
      dfs(node)

    result = 0
    for node in range(1, num_nodes):
      result += ceil(num_reps_leaving[node] / seats)

    return result
