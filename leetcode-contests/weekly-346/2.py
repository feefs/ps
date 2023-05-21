# 2697. Lexicographically Smallest Palindrome
class Solution:
  def makeSmallestPalindrome(self, s: str) -> str:
    chars = list(s)
    i, j = 0, len(s) - 1
    while i < j:
      if chars[i] != chars[j]:
        if chars[i] < chars[j]:
          chars[j] = chars[i]
        else:
          chars[i] = chars[j]
      i += 1
      j -= 1

    return "".join(chars)
