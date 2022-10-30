# 2443. Sum of Number and Its Reverse
class Solution:
  def sumOfNumberAndReverse(self, num: int) -> bool:
    for n in range(min(num + 1, int(10e5) + 1)):
      if n + int(str(n)[::-1]) == num:
        return True

    return False
