# 2646. Minimize the Total Price of the Trips
class Solution:
  def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int],
                        trips: List[List[int]]) -> int:
    """
    compute the cost each node will contribute to the final result
      traverse all paths and count the number of times a node is touched
      multiply each node by the number of times it's touched
    dfs
      compute an extra dfs path if the current node can be halved
      since the graph is a tree, use a prev parameter and @cache to speed up computation
    """
    graph, counts = defaultdict(set), defaultdict(int)
    for a, b in edges:
      graph[a].add(b)
      graph[b].add(a)

    def count_path_nodes(start, end):
      def dfs(curr, prev):
        if curr == end:
          counts[curr] += 1
          return True
        for neighbor in graph[curr]:
          if neighbor != prev and dfs(neighbor, curr):
            counts[curr] += 1
            return True
        return False

      dfs(start, None)

    for start, end in trips:
      count_path_nodes(start, end)

    prices = {i: p for i, p in enumerate(price)}
    costs = {i: prices[i] * counts[i] for i in range(n)}

    @cache
    def dfs(curr, prev, can_halve):
      curr_cost = costs[curr]
      result = float('inf')
      valid_neighbors = list(
          filter(lambda neighbor: neighbor != prev, graph[curr]))
      if can_halve:
        result = min(
            result, (curr_cost // 2) +
            sum([dfs(neighbor, curr, False) for neighbor in valid_neighbors]))
      result = min(
          result, curr_cost +
          sum([dfs(neighbor, curr, True) for neighbor in valid_neighbors]))
      return result

    return dfs(0, None, True)
