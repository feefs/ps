# 2588. Count the Number of Beautiful Subarrays
class Solution:
  def beautifulSubarrays(self, nums: List[int]) -> int:
    """
    a subarray is beautiful if the count of each bit across all numbers is even
    repeatedly pair up numbers that have the same bit value and flip both to 0 (subtract 2^k)
    observation: xor'ing all elements and testing if it's equal to 0 achieves the same thing
    same approach as 560. Subarray Sum Equals K, but with xors instead of sums
    """
    prefix_xors = defaultdict(int, {0: 1})
    result = 0
    curr_xor = 0
    for n in nums:
      curr_xor ^= n
      """
      [        ] curr_xor
      [  ]       prefix_xor
          [    ] curr_xor ^ prefix_xor
      curr_xor ^ prefix_xor is a subarray that may be beautiful (xors to 0)
      rearrange curr_xor ^ prefix_xor = 0
        (curr_xor ^ prefix_xor) ^ prefix_xor = (0) ^ prefix_xor
        curr_xor = prefix_xor
        => check curr_xor exists to get count of right side (number of beautiful subarrays)
      """
      if curr_xor in prefix_xors:
        result += prefix_xors[curr_xor]
      prefix_xors[curr_xor] += 1

    return result
