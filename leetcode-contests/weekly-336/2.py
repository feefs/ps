# 2587. Rearrange Array to Maximize Prefix Score
class Solution:
  def maxScore(self, nums: List[int]) -> int:
    hp = [-n for n in nums]
    heapq.heapify(hp)
    score, curr = 0, 0
    while hp:
      val = -1 * heapq.heappop(hp)
      curr += val
      # curr going below 0 means it can never be positive again
      # this is because hp is a max heap
      if curr < 0:
        break
      # handle edge case where largest value in nums is 0
      if curr > 0:
        score += 1

    return score
