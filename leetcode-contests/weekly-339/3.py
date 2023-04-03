# 2611. Mice and Cheese
class Solution:
  def miceAndCheese(self, reward1: List[int], reward2: List[int],
                    k: int) -> int:
    result = 0
    # k rewards must be eaten by mouse 1, n - k rewards must be eaten by the second
    # sort by the difference between the rewards, and pick the first k for mouse 1 to eat
    for i, choice in enumerate(
        sorted(zip(reward1, reward2),
               key=lambda choice: choice[1] - choice[0])):
      if i < k:
        result += choice[0]
      else:
        result += choice[1]

    return result
