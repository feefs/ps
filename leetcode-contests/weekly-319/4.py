# 2472. Maximum Number of Non-overlapping Palindrome Substrings
class Solution:
  class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
      """
      greedily extract palindromes from s
      """

      # returns if s[start:end] is a palindrome
      def valid_palindrome(start, end):
        l, r = start, end - 1
        if r >= len(s):
          return False
        while l < r:
          if s[l] != s[r]:
            return False
          l += 1
          r -= 1
        return True

      result = 0
      i = 0
      while i < len(s):
        if valid_palindrome(i, i + k):
          result += 1
          i += k
        elif valid_palindrome(i, i + k + 1):
          result += 1
          i += k + 1
        else:
          i += 1

      return result

  def maxPalindromes(self, s: str, k: int) -> int:
    """
    TLE
    Compute intervals of palindromes length >= k
    Find the maximum number of non-overlapping intervals
    """
    palindromes = set()

    def expand(l, r):
      if l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 >= k:
          palindromes.add((l, r))
        expand(l - 1, r + 1)

    for i in range(len(s)):
      expand(i, i)
      expand(i, i + 1)

    if len(palindromes) == 0:
      return 0

    intervals = list(palindromes)
    intervals.sort(key=lambda i: i[1])

    result = 0
    prev = intervals[0]
    for curr in intervals[1:]:
      if curr[0] <= prev[1]:
        if curr[1] < prev[1]:
          prev[1] = curr[1]
      else:
        result += 1
        prev = curr
    result += 1

    return result
