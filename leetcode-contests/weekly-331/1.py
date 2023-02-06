# 2558. Take Gifts From the Richest Pile
class Solution:
  def pickGifts(self, gifts: List[int], k: int) -> int:
    pq = [-n for n in gifts]
    heapq.heapify(pq)
    while k:
      v = -1 * heapq.heappop(pq)
      heapq.heappush(pq, -1 * int(math.sqrt(v)))
      k -= 1

    return -1 * sum(pq)
