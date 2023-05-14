# 2682. Find the Losers of the Circular Game
class Solution:
  def circularGameLosers(self, n: int, k: int) -> List[int]:
    received = set()
    friend_index, turn = 0, 1

    while friend_index + 1 not in received:
      received.add(friend_index + 1)
      friend_index = (friend_index + (k * turn)) % n
      turn += 1

    result = []
    for i in range(1, n + 1):
      if i not in received:
        result.append(i)

    return result
