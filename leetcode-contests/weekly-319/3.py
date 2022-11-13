# 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def minimumOperations(self, root: Optional[TreeNode]) -> int:
    # https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array
    def min_swaps(l):
      sorted_pairs = list(sorted(enumerate(l), key=lambda p: p[1]))
      result = 0
      visited = set()
      for target_index, (original_index, _) in enumerate(sorted_pairs):
        if original_index in visited:
          continue
        cycle_length = 0
        curr = original_index
        while curr not in visited:
          visited.add(curr)
          cycle_length += 1
          curr = sorted_pairs[curr][0]
        result += cycle_length - 1
      return result

    result = 0
    q = deque([root])
    while q:
      q2 = deque([])
      while q:
        curr = q.popleft()
        if curr.left:
          q2.append(curr.left)
        if curr.right:
          q2.append(curr.right)
      result += min_swaps(map(lambda n: n.val, q2))
      q = q2

    return result
