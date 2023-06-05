# 2717. Semi-Ordered Permutation
class Solution:
  def semiOrderedPermutation(self, nums: List[int]) -> int:
    n = len(nums)
    one_index = nums.index(1)
    n_index = nums.index(n)

    return one_index + (n - n_index - 1) - (1 if one_index > n_index else 0)
