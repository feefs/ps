# 2550. Count Collisions of Monkeys on a Polygon
class Solution:
  def monkeyMove(self, n: int) -> int:
    # the monkeys can move in 2 ** n ways
    # there are two ways for no monkeys to collide (all clockwise, all counterclockwise)
    # answer is ((2 ** n) - 2) % ((10 ** 9) + 7)
    mod = (10**9) + 7

    return (pow(2, n, mod) - 2) % mod
