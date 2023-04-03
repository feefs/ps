# 2609. Find the Longest Balanced Substring of a Binary String
class Solution:
  def findTheLongestBalancedSubstring(self, s: str) -> int:
    chars = list(reversed(s))
    result = 0
    i = 0
    while i < len(chars):
      c = chars[i]
      if c == '0':
        j = i - 1
        while i < len(s) and j >= 0 and chars[i] == '0' and chars[j] == '1':
          result = max(result, i - j + 1)
          i += 1
          j -= 1
      i += 1

    return result
