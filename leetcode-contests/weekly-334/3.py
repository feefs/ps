# 2576. Find the Maximum Number of Marked Indices
class Solution:
  def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
    """
    greedy approach
      sort and precompute i and j candidate values
      pair as many values together as possible
    """
    N = len(nums)
    nums.sort()
    # if nums is odd, start j_candidates at ceil(N / 2) to avoid overlapping indices
    j_candidates = nums[N - (N // 2):]
    i_candidates = [nums[i] * 2 for i in range(N // 2)]

    result = 0
    i, j = 0, 0
    while i < len(i_candidates) and j < len(j_candidates):
      i_cand, j_cand = i_candidates[i], j_candidates[j]
      if i_cand <= j_cand:
        result += 2
        i += 1
        j += 1
      else:
        j += 1

    return result
