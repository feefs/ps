# 2673. Make Costs of Paths Equal in a Binary Tree
class Solution:
  def minIncrements(self, n: int, cost: List[int]) -> int:
    # shift cost to index using the node number i
    cost = [0] + cost

    # compute path with biggest cost
    def dfs(i, path_cost):
      if (2 * i) - 1 >= n:
        return path_cost + cost[i]
      path_cost += cost[i]
      return max(dfs(2 * i, path_cost), dfs((2 * i) + 1, path_cost))

    target_cost = dfs(1, 0)

    result = 0

    # returns the number of times a node needs to be incremented
    def dfs(i, remaining):
      nonlocal result
      if (2 * i) - 1 >= n:
        result += remaining - cost[i]
        return remaining - cost[i]
      l, r = dfs((2 * i), remaining - cost[i]), dfs((2 * i) + 1,
                                                    remaining - cost[i])
      """
      if both child nodes are incremented more than once
        increment the current node min(l, r) times
        decrement both child nodes min(l, r) times
      update the global increment count accordingly
      """
      curr_increments = min(l, r)
      result -= 2 * min(l, r)
      result += curr_increments
      return curr_increments

    dfs(1, target_cost)

    return result
