# 2595. Number of Even and Odd Bits
class Solution:
  def evenOddBit(self, n: int) -> List[int]:
    even, odd = 0, 0
    even_bit = True
    while n:
      if n & 1:
        if even_bit:
          even += 1
        else:
          odd += 1
      even_bit = not even_bit
      n >>= 1

    return even, odd
