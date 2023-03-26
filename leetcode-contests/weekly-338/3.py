# 2602. Minimum Operations to Make All Array Elements Equal
class Solution:
  def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
    """
    for a given query q
      we need to increase elements less than q and decrease elements greater than q
    sort the array and compute its prefix sums
      binary search the array to find the split point
        expected sum in each half is q * # of elements in each half
      use prefix sum to find the sum of values in each half
    """
    nums.sort()
    # prefix[i] = prefix sum of elements nums[:i]
    prefix = [0]
    curr = 0
    for n in nums:
      curr += n
      prefix.append(curr)

    # binary search for split point
    # returns the index where we would insert q
    def split_point(q):
      l, r = 0, len(nums)
      while l < r:
        mid = (l + r) // 2
        if nums[mid] < q:
          l = mid + 1
        else:
          r = mid
      return l

    result = []
    for q in queries:
      split = split_point(q)
      l_expected_sum = split * q
      r_expected_sum = (len(nums) - split) * q
      # prefix[-1] = the total prefix sum
      # subtract the left prefix sum from it to get the right half
      l_sum, r_sum = prefix[split], prefix[-1] - prefix[split]
      result.append((l_expected_sum - l_sum) - (r_expected_sum - r_sum))

    return result
