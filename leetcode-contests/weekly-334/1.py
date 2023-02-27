# 2574. Left and Right Sum Differences
class Solution:
  def leftRigthDifference(self, nums: List[int]) -> List[int]:
    left, right = [], deque([])
    curr = 0
    for n in nums:
      left.append(curr)
      curr += n
    curr = 0
    for n in reversed(nums):
      right.appendleft(curr)
      curr += n

    return [abs(left[i] - right[i]) for i in range(len(nums))]
