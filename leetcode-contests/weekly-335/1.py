# 2582. Pass the Pillow
class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    indices = [i for i in range(1, n + 1)] + [i for i in reversed(range(2, n))]

    return indices[time % len(indices)]
