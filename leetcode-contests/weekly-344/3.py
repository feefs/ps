# 2672. Number of Adjacent Elements With the Same Color
class Solution:
  def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
    result = []
    colors = [0 for _ in range(n)]
    adj = set()
    for i, color in queries:
      colors[i] = color
      # check if setting the color removed adjacent elements
      if i in adj and colors[i + 1] != color:
        adj.remove(i)
      if i - 1 in adj and colors[i - 1] != color:
        adj.remove(i - 1)
      # check if setting the color created adjacent elements
      if i > 0 and colors[i - 1] == color:
        adj.add(i - 1)
      if i < n - 1 and colors[i + 1] == color:
        adj.add(i)
      result.append(len(adj))

    return result
