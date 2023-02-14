# 2565. Subsequence With the Minimum Score
class Solution:
  def minimumScore(self, s: str, t: str) -> int:
    """
    compute prefixes and suffixes of t, where each of them is a subsequence of s
      find the pair where the end of the prefix and the start of the suffix are closest
    left[li] = z, the leftmost index in s where t[:li + 1] is a subsequence of s[:lz + 1]
      lz can have the value len(s), meaning it's impossible
    right[ri] = z, the rightmost index in s where t[ri:] is a subsequence of s[rz:]
      rz can have the value -1, meaning it's impossible
    left = li + 1, right = ri - 1
    """
    s_len, t_len = len(s), len(t)
    result = t_len

    left = [s_len] * t_len
    li, z = 0, 0
    while z < s_len and li < t_len:
      c = s[z]
      if c == t[li]:
        # try right = len(t) - 1, which is removing values t[li + 1:]
        result = min(result, (t_len - 1) - (li + 1) + 1)
        left[li] = z
        li += 1
      z += 1
    right = [-1] * t_len
    ri, z = t_len - 1, s_len - 1
    while z >= 0 and ri >= 0:
      c = s[z]
      if c == t[ri]:
        # try left = 0, which is removing values t[:ri]
        result = min(result, (ri - 1) - (0) + 1)
        right[ri] = z
        ri -= 1
      z -= 1

    # examine pairs, use two pointers since values are monotonically increasing in left and right
    li = 0
    # ensure valid ri values by starting at the first index that isn't -1 in right
    for ri in range(bisect_right(right, -1), t_len):
      # if the pair wouldn't remove at least one letter in t,
      # or if li is invalid,
      # or if the prefix and suffix subsequences s[:lz + 1] and s[rz:] are overlapping
      # skip to the next ri value
      if li >= ri - 1 or left[li] == s_len or left[li] >= right[ri]:
        continue
      # advance li rightwards while maintaining the opposite of the three conditions above
      while li < ri - 1 and left[li + 1] != s_len and left[li + 1] < right[ri]:
        li += 1
      result = min(result, (ri - 1) - (li + 1) + 1)

    return result
