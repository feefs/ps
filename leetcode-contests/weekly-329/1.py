# 2544. Alternating Digit Sum
class Solution:
  def alternateDigitSum(self, n: int) -> int:
    result = 0
    sign = True
    for string_digit in str(n):
      digit = int(string_digit)
      result += (1 if sign else -1) * digit
      sign = not sign

    return result
