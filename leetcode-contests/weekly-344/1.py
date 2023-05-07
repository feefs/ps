# 2670. Find the Distinct Difference Array
class Solution:
  def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
    pre = []
    s = set()
    for n in nums:
      s.add(n)
      pre.append(len(s))
    suf = deque([])
    s = set()
    for n in reversed(nums):
      suf.appendleft(len(s))
      s.add(n)
    result = []
    for i in range(len(nums)):
      result.append(pre[i] - suf[i])

    return result
