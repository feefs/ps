# 2509. Cycle Length Queries in a Tree
class Solution:
  def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    """
    floor divide a node's value by two to move up a node
    meet at node 1, count the number of edges traversed along the way
    top down dp to only traverse the paths we need
    cache to reuse values of previously traversed paths
    """
    @cache
    def f(a, b):
      if a == b:
        return 1
      if a > b:
        a, b = b, a
      return 1 + f(a, b // 2)

    return [f(a, b) for a, b in queries]
