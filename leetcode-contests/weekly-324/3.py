# 2508. Add Edges to Make Degrees of All Nodes Even
class Solution:
  def isPossible(self, n: int, edges: List[List[int]]) -> bool:
    degree_counts = defaultdict(int)
    graph = defaultdict(set)
    for a, b in edges:
      graph[a].add(b)
      graph[b].add(a)
      degree_counts[a] += 1
      degree_counts[b] += 1

    odd_degrees = [
        node for node, degree in degree_counts.items() if degree % 2 == 1
    ]

    if len(odd_degrees) == 0:
      return True
    elif len(odd_degrees) == 2:
      node1, node2 = odd_degrees
      if node1 not in graph[node2]:
        return True
      # search for a node that can connect to both of these nodes
      for node in range(1, n + 1):
        if node1 not in graph[node] and node2 not in graph[node]:
          return True
      return False
    elif len(odd_degrees) == 4:
      node1, node2, node3, node4 = odd_degrees

      # try four pairings, a pairing works if an edge doesn't already exist between them
      #     # 1-2 3-4
      #     # 1-3 2-4
      #     # 1-4 2-3
      def check_pairing(p1, p2):
        return p1[0] not in graph[p1[1]] and p2[0] not in graph[p2[1]]

      if check_pairing([node1, node2], [node3, node4]):
        return True
      if check_pairing([node1, node3], [node2, node4]):
        return True
      if check_pairing([node1, node4], [node2, node3]):
        return True
      return False
    else:
      return False
