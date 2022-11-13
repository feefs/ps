# 2470. Number of Subarrays With LCM Equal to K
class Solution:
  def subarrayLCM(self, nums: List[int], k: int) -> int:
    result = 0
    for i in range(len(nums)):
      curr_lcm = nums[i]
      for j in range(i, len(nums)):
        curr_lcm = math.lcm(curr_lcm, nums[j])
        if curr_lcm == k:
          result += 1

    return result
