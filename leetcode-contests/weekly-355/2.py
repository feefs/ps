# 2789. Largest Element in an Array after Merge Operations
class Solution:
  def maxArrayValue(self, nums: List[int]) -> int:
    # try to merge the biggest number starting from the back
    n = len(nums)
    curr = nums[-1]
    result = curr
    i = n - 1
    while i > 0:
      if nums[i - 1] <= curr:
        # apply the merge operation on nums[i - 1]
        curr += nums[i - 1]
      else:
        # the merge operation cannot be applied on nums[i - 1]
        curr = nums[i - 1]
      result = max(result, curr)
      i -= 1

    return result
