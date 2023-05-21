# 2699. Modify Graph Edge Weights
class Solution:
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int,
                         destination: int, target: int) -> List[List[int]]:
    graph = defaultdict(set)
    for a, b, w in edges:
      graph[a].add((b, w))
      graph[b].add((a, w))

    # dijkstras with a negative_substitute parameter that treats all -1 edges as that value
    def dijkstras(start, negative_substitute):
      dist = defaultdict(lambda: float('inf'))
      dist[start] = 0
      prev = {}
      pq = [(0, start)]
      while pq:
        d, a = heapq.heappop(pq)
        # outdated value (a shorter path to a exists)
        if dist[a] < d:
          continue
        for b, w in graph[a]:
          if w == -1:
            w = negative_substitute
          if dist[b] > d + w:
            dist[b] = d + w
            prev[b] = a
            heapq.heappush(pq, (dist[b], b))
      return dist, prev

    """
    if a shortest path with only positive edges exists and has a distance less than target
      there is no other shortest path with a distance of target, otherwise it would contradict
    substitute negative edges with float('inf') to simulate them not existing
    """
    no_neg_dist, _ = dijkstras(source, float('inf'))
    if no_neg_dist[destination] < target:
      return []
    """
    we must substitute all negative edges, and the smallest value is 1
    if the shortest path still overshoots target
      there is no shortest path with a distance of target, since substituted edges can't decrease further
    """
    dist, prev = dijkstras(source, 1)
    if dist[destination] > target:
      return []

    # extract the path
    path = deque([destination])
    curr = destination
    while curr != source:
      path.appendleft(prev[curr])
      curr = prev[curr]

    # map node pairs to edges
    mapped_edges = {(min(a, b), max(a, b)): w for a, b, w in edges}

    def get_edge(a, b):
      return mapped_edges[(min(a, b), max(a, b))]

    def set_edge(a, b, w):
      mapped_edges[(min(a, b), max(a, b))] = w

    """
    for the current node, next node, and edge weight a, b, and w
      src --- ... --- a --- b --- dest
                         w
      [   path_sum    ]
                      [  remaining   ]
      w must be large enough such that future edges we increase between b and dest to reach target
      don't result in a new shortest path from b to dest being formed
      if w equals -1
        remaining = target - path_sum
        remaining - w <= (b --- dest)
        w >= remaining - (b --- dest)
          (b --- dest) can be computed by running dijkstras again for each b
          however, it's the same as (dest --- b) so just run dijkstras once from destination
    """
    reverse_dist, _ = dijkstras(destination, float('inf'))
    path_sum = 0
    for i in range(len(path) - 1):
      a, b = path[i], path[i + 1]
      remaining = target - path_sum
      if get_edge(a, b) == -1:
        set_edge(a, b, min(max(remaining - reverse_dist[b], 1), 2 * (10**9)))
      path_sum += get_edge(a, b)

    # set all other -1 edges to 2 * (10 ** 9) to avoid creating another shortest path
    for a, b in mapped_edges:
      if get_edge(a, b) == -1:
        set_edge(a, b, 2 * (10**9))

    return [[a, b, w] for (a, b), w in mapped_edges.items()]
