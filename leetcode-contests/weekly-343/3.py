# 2662. Minimum Cost of a Path With Special Roads
class Solution:
  def minimumCost(self, start: List[int], target: List[int],
                  specialRoads: List[List[int]]) -> int:
    # dfs with pruning
    start, target = (start[0], start[1]), (target[0], target[1])

    def dist(a, b):
      return abs(a[0] - b[0]) + abs(a[1] - b[1])

    result = dist(start, target)
    distance = defaultdict(lambda: float('inf'))

    def dfs(pos, cost):
      nonlocal result
      """
      prune if
        the current path to pos is worse than the best path to target so far
        the current path to pos is worse than the best path to pos so far
      """
      if cost > result or cost >= distance[pos]:
        return

      distance[pos] = cost
      result = min(result, cost + dist(pos, target))

      for i, j, k, l, c in specialRoads:
        a, b = (i, j), (k, l)
        # travel to a, then b with cost c
        dfs(b, cost + dist(pos, a) + c)

    dfs(start, 0)

    return result
