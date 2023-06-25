# 2750. Ways to Split Array Into Good Subarrays
class Solution:
  def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
    """
    a "bar" must be placed in one of the gaps between ones
    the number of gaps between two ones is the number of zeros + 1
    the total number of possibilities is all these gaps multiplied together
    """
    # shave off zeros from both sides
    nums = deque(nums)
    while nums and nums[0] == 0:
      nums.popleft()
    while nums and nums[-1] == 0:
      nums.pop()
    if len(nums) == 0:
      return 0
    # compute and multiply gaps
    result = 1
    zeros = 0
    for n in nums:
      if n == 1:
        result = (result * (zeros + 1)) % ((10**9) + 7)
        zeros = 0
      else:
        zeros += 1

    return result
