# 2663. Lexicographically Smallest Beautiful String
class Solution:
  def smallestBeautifulString(self, s: str, k: int) -> str:
    """
    for any index i
      s[i] != s[i - 1] and s[i] != s[i - 2] <=> s[:i + 1] is beautiful
    increment a base k number until it is beautiful
    """
    digits = [ord(c) - ord('a') for c in s]

    def is_beautiful(i):
      if i > 1:
        return (digits[i] != digits[i - 1]) and (digits[i] != digits[i - 2])
      elif i > 0:
        return digits[i] != digits[i - 1]
      else:
        return True

    i = len(digits) - 1
    digits[i] += 1
    while 0 <= i < len(digits):
      if digits[i] == k:
        # carry the digit
        digits[i] = 0
        i -= 1
        digits[i] += 1
      elif not is_beautiful(i):
        digits[i] += 1
      else:
        i += 1

    return "" if i < 0 else "".join([chr(d + ord('a')) for d in digits])
