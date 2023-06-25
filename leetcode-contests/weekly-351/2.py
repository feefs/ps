# 2749. Minimum Operations to Make the Integer Zero
class Solution:
  def makeTheIntegerZero(self, num1: int, num2: int) -> int:
    """
    sum1 - (n powers of two summation) - (n * sum2) = 0
    (n powers of two summation) = sum1 - (n * sum2)
    find value of n where the above equation is satisfied
    """
    n = 1
    while True:
      target = num1 - (n * num2)
      """
      if n becomes larger than target and num2 is positive
        target can only get smaller and n can only become larger
        => no way for n to ever fall into the range [target.bit_count(), target]
      """
      if n > target and num2 > 0:
        return -1
      """
      minimum number of powers of two summed together to make target is the bit count
      maximum number of powers of two summed together to make target is target (all ones)
      check if n is in that range
      """
      if target.bit_count() <= n <= target:
        return n
      n += 1
