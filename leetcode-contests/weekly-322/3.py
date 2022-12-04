# 2492. Minimum Score of a Path Between Two Cities
class Solution:
  def minScore(self, n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(lambda: set())
    for r in roads:
      a, b, d = r
      graph[a].add((b, d))
      graph[b].add((a, d))

    result = float('inf')
    # we only care about checking all edges in the connected component containing 1, not all possible paths
    # use an "added" set instead of a "visited/expanded" set to speed things up
    added = set([1])
    q = deque([1])
    while q:
      curr = q.popleft()
      for child, d in graph[curr]:
        if child not in added:
          q.append(child)
          added.add(child)
        result = min(result, d)

    return result
