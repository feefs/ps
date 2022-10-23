# 2448. Minimum Cost to Make Array Equal
class Solution:
  def minCost(self, nums: List[int], cost: List[int]) -> int:
    """
    there must be a value in nums that we do not change
      all numbers below must increase to this value
      all numbers above must decrease to this value
    for each number, compute how much it costs to raise all values below to it
    repeat for how much it costs to lower all values above to it
    actual cost for a value is the pairwise sum to raise all below and lower all above
      take the min of these values
    """
    values = list(sorted(zip(nums, cost)))
    N = len(nums)

    l_costs = [0] * N
    prev_height, cost_to_raise_all_prev = values[0]
    for i, (n, c) in enumerate(values[1:], 1):
      l_costs[i] += l_costs[i - 1] + (cost_to_raise_all_prev *
                                      (n - prev_height))
      cost_to_raise_all_prev += c
      prev_height = n

    r_costs = [0] * N
    after_height, cost_to_lower_all_after = values[-1]
    for i, (n, c) in reversed(list(enumerate(values[:-1]))):
      r_costs[i] += r_costs[i + 1] + (cost_to_lower_all_after *
                                      (after_height - n))
      cost_to_lower_all_after += c
      after_height = n

    return min(map(lambda c: c[0] + c[1], zip(l_costs, r_costs)))
