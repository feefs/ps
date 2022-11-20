# 2476. Closest Nodes Queries in a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def closestNodes(self, root: Optional[TreeNode],
                   queries: List[int]) -> List[List[int]]:
    values = []

    def dfs(curr):
      if not curr:
        return
      dfs(curr.left)
      values.append(curr.val)
      dfs(curr.right)

    dfs(root)

    def bs(q):
      l, r = 0, len(values)
      while l < r:
        mid = (l + r) // 2
        if values[mid] < q:
          l = mid + 1
        else:
          r = mid
      if l < len(values) and values[l] == q:
        return [q, q]
      else:
        return [
            values[l - 1] if l > 0 else -1, values[l] if l < len(values) else -1
        ]

    return [bs(q) for q in queries]
