# 2735. Collecting Chocolates
class Solution:
  def minCost(self, nums: List[int], x: int) -> int:
    n = len(nums)
    rot_cost = 0
    result = sum(nums)
    curr_nums = nums
    for offset in range(1, n):
      rot_cost += x
      next_nums = curr_nums[:]
      # update the best cost chocolate c could have been bought at
      # chocolate c's actual location is (c - offset) % n
      for i in range(n):
        next_nums[i] = min(curr_nums[i], curr_nums[(i + 1) % n])
      # factor in the rotation cost and update the best buying configuration
      result = min(result, rot_cost + sum(next_nums))
      curr_nums = next_nums

    return result
