# 2610. Convert an Array Into a 2D Array With Conditions
class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    # count the numbers and sort by count descending
    # the minimum number of rows is the maximum count of a number
    counts = Counter(nums)
    result = [[] for _ in range(max(counts.values()))]
    for n, count in sorted(counts.items(),
                           key=lambda pair: pair[1],
                           reverse=True):
      for c in range(count):
        result[c].append(n)

    return result
