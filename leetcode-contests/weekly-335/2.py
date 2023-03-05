# 2583. Kth Largest Sum in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
    sums = []
    q = deque([root])
    while q:
      next_q = deque([])
      level_sum = sum([node.val for node in q])
      if len(sums) < k:
        heapq.heappush(sums, level_sum)
      elif sums[0] < level_sum:
        heapq.heappushpop(sums, level_sum)
      while q:
        curr = q.popleft()
        if curr.left:
          next_q.append(curr.left)
        if curr.right:
          next_q.append(curr.right)
      q = next_q

    return sums[0] if len(sums) == k else -1
