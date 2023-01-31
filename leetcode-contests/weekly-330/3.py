# 2551. Put Marbles in Bags
class Solution:
  def putMarbles(self, weights: List[int], k: int) -> int:
    # divider_values contains how much the total score will increase by when adding a divider
    # putting in a divider between i and i + 1 will increase the score by weights[i] and weights[i + 1]
    divider_values = [
        weights[i] + weights[i + 1] for i in range(len(weights) - 1)
    ]
    # find k - 1 divider_values that increase the score by the most and least and subtract them
    divider_values.sort()

    return sum(divider_values[len(weights) - 1 -
                              (k - 1):]) - sum(divider_values[:k - 1])

  def putMarbles(self, weights: List[int], k: int) -> int:
    """
    TLE
    DP
    """
    # f(i, j, k) = (min_score, max_score) with marbles weights[i:j + 1] and k bags
    @cache
    def f(i, j, k):
      if k == 1:
        return weights[i] + weights[j], weights[i] + weights[j]
      min_s, max_s = float('inf'), float('-inf')
      for divider in range(i, j):
        left_score = weights[i] + weights[divider]
        right_min_s, right_max_s = f(divider + 1, j, k - 1)
        min_s = min(min_s, left_score + right_min_s)
        max_s = max(max_s, left_score + right_max_s)
      return min_s, max_s

    min_score, max_score = f(0, len(weights) - 1, k)

    return max_score - min_score
