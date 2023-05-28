# 2710. Remove Trailing Zeros From a String
class Solution:
  def removeTrailingZeros(self, num: str) -> str:
    chars = list(num)
    while chars and chars[-1] == '0':
      chars.pop()

    return "".join(chars)
