# 2771. Longest Non-decreasing Subarray From Two Arrays
class Solution:
  def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    # dp1[i]/dp2[i] = longest non-decreasing subarray that ends at and includes the value at nums1[i]/nums2[i]
    dp1 = [1 for _ in range(n)]
    dp2 = [1 for _ in range(n)]
    for i in range(1, n):
      n1, n2 = nums1[i], nums2[i]
      pn1, pn2 = nums1[i - 1], nums2[i - 1]
      if n1 >= pn1:
        dp1[i] = max(dp1[i], 1 + dp1[i - 1])
      if n1 >= pn2:
        dp1[i] = max(dp1[i], 1 + dp2[i - 1])
      if n2 >= pn1:
        dp2[i] = max(dp2[i], 1 + dp1[i - 1])
      if n2 >= pn2:
        dp2[i] = max(dp2[i], 1 + dp2[i - 1])

    return max(max(dp1), max(dp2))
