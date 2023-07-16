# 2780. Minimum Index of a Valid Split
class Solution:
  def minimumIndex(self, nums: List[int]) -> int:
    # find the dominant element
    dom, count = list(sorted(Counter(nums).items(),
                             key=lambda item: item[1]))[-1]

    n = len(nums)
    m1, m2 = 1, n - 1
    dom_count1, dom_count2 = (1 if nums[0] == dom else
                              0), count - (1 if nums[0] == dom else 0)

    # test each split to see if the dominant element of nums is also the dominant element of both arrays
    i = 0
    while i < n - 1 and not ((dom_count1 > m1 // 2) and (dom_count2 > m2 // 2)):
      i += 1
      dom_count1 += (1 if nums[i] == dom else 0)
      dom_count2 -= (1 if nums[i] == dom else 0)
      m1 += 1
      m2 -= 1

    return i if i < n - 1 else -1
