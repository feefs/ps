# 2458. Height of Binary Tree After Subtree Removal Queries
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def treeQueries(self, root: Optional[TreeNode],
                  queries: List[int]) -> List[int]:
    """
    for each node, store the maximum height that can be reached if we continue dfs
      call it depth
    dfs again to compute the value if a node is removed
      keep track of a variable called deepest_other_depth, the larger value between
        the current node's sibling's depth
        the depth of the subtree that doesn't contain any of the current node's ancestors
      if neither of the two exist, deepest_other_depth will be float('-inf')
      set the current node's value if removed to be the larger value between deepest_other_depth and depth - 1
      update deepest_other_depth for left and right children when recursing
    compute answers for the queries
    """
    depths, if_removed = {}, {}
    get_depth = lambda node: depths[node.val] if node else float('-inf')

    def dfs(curr, depth):
      depths[curr.val] = max(
          dfs(curr.left, depth + 1) if curr.left else depth,
          dfs(curr.right, depth + 1) if curr.right else depth)
      return depths[curr.val]

    dfs(root, 0)

    def dfs(curr, deepest_other_depth, depth):
      if not curr:
        return
      if_removed[curr.val] = max(deepest_other_depth, depth - 1)
      dfs(curr.left, max(get_depth(curr.right), deepest_other_depth), depth + 1)
      dfs(curr.right, max(get_depth(curr.left), deepest_other_depth), depth + 1)

    dfs(root, float('-inf'), 0)

    return [if_removed[q] for q in queries]
