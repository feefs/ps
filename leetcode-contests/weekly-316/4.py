# 2449. Minimum Number of Operations to Make Arrays Similar
class Solution:
  def makeSimilar(self, nums: List[int], target: List[int]) -> int:
    """
    divide into evens and odds since they interact independently
    sort nums and target, pair up numbers to compute number of sub-operations needed
      greedy argument, we would need more sub-operations if we swapped the order
    the number of sub-operations to match n to t is abs(n - t) // 2
      this is because we can increment or decrement a value in nums by 2
    the number of operations needed is the total number of sub-operations // 2
      this is because we can perform two sub-operations in one operation
    """
    n_evens, n_odds = [], []
    for n in sorted(nums):
      if n % 2 == 0:
        n_evens.append(n)
      else:
        n_odds.append(n)

    t_evens, t_odds = [], []
    for t in sorted(target):
      if t % 2 == 0:
        t_evens.append(t)
      else:
        t_odds.append(t)

    result = 0
    for n, t in zip(n_evens, t_evens):
      result += abs(n - t) // 2

    for n, t in zip(n_odds, t_odds):
      result += abs(n - t) // 2

    return result // 2
