# 2772. Apply Operations to Make All Array Elements Equal to Zero
class Solution:
  def checkArray(self, nums: List[int], k: int) -> bool:
    n = len(nums)
    d = {}
    curr_subs = 0
    for i, v in enumerate(nums):
      # undo subtraction count required by a previous value
      if i in d:
        curr_subs -= d[i]
      if v < curr_subs:
        # nums[i] can't be set to 0 if it's less than the currently required subtraction count
        return False
      elif v > curr_subs:
        # the subtraction count can't be increased if we can't move the subarray further to the right
        if i + k > n:
          return False
        # store amount to undo the subtraction count by once the loop reaches index i + k
        d[i + k] = v - curr_subs
        # increase the subtraction count to v, the value of the subarray starting at index i
        curr_subs = v

    return True
