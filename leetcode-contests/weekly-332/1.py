# 2562. Find the Array Concatenation Value
class Solution:
  def findTheArrayConcVal(self, nums: List[int]) -> int:
    result = 0
    values = deque(nums)
    while len(values) > 1:
      result += int(str(values.popleft()) + str(values.pop()))
    if values:
      result += values.pop()

    return result
