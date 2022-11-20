# 2475. Number of Unequal Triplets in Array
class Solution:
  def unequalTriplets(self, nums: List[int]) -> int:
    N = len(nums)
    result = 0
    for i in range(N):
      for j in range(i + 1, N):
        for k in range(j + 1, N):
          if len(set([nums[i], nums[j], nums[k]])) == 3:
            result += 1

    return result
