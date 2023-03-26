# 2603. Collect Coins in a Tree
class Solution:
  def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
    """
    compute the "minimal" tree, which contains all the nodes we need to visit in order to collect all coins
      we need to visit every node and return to the start
        => every node is visited exactly twice
        => answer is 2 * number of edges
    repeatedly prune leaves that don't contain coins
      these leaves only increase the size of the "minimal" tree with no benefit
    prune leaves twice, since we can reach them from two nodes away
    """
    graph = defaultdict(set)
    for a, b in edges:
      graph[a].add(b)
      graph[b].add(a)

    # removes the leaf and returns its neighbor still in the tree
    def prune(leaf):
      neighbor = list(graph[leaf])[0]
      graph[leaf].remove(neighbor)
      graph[neighbor].remove(leaf)
      return neighbor

    # iterating through a filter while pruning the graph can lead to errors due to lazy computation
    # wrap filter in a list to avoid this issue
    def leaves():
      return list(filter(lambda node: len(graph[node]) == 1, range(len(coins))))

    # prune leaves that don't contain coins
    for leaf in leaves():
      node = leaf
      # pruning a leaf can create another leaf, so repeatedly prune them
      while len(graph[node]) == 1 and coins[node] == 0:
        node = prune(node)

    # prune the remaining leaves twice to create the minimal tree
    for _ in range(2):
      for leaf in leaves():
        # it's possible for a previous iteration to have already removed the current leaf
        # handle the edge case here since prune() itself doesn't
        if len(graph[leaf]) == 1:
          prune(leaf)

    # this double counts the number of edges, so no need to multiply by two
    return sum([len(neighbors) for neighbors in graph.values()])
