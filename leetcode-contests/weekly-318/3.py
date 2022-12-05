# 2462. Total Cost to Hire K Workers
class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    l_add, r_add = candidates, len(costs) - candidates - 1
    if l_add >= r_add:
      heapq.heapify(costs)
      return sum([heapq.heappop(costs) for _ in range(k)])

    l, r = [n for n in costs[:candidates]
            ], [n for n in costs[len(costs) - candidates:]]
    heapq.heapify(l)
    heapq.heapify(r)

    result = 0
    while k > 0 and l_add <= r_add:
      if l[0] <= r[0]:
        result += heapq.heappop(l)
        heapq.heappush(l, costs[l_add])
        l_add += 1
      else:
        result += heapq.heappop(r)
        heapq.heappush(r, costs[r_add])
        r_add -= 1
      k -= 1

    if k > 0:
      both = l + r
      heapq.heapify(both)
      while k > 0:
        result += heapq.heappop(both)
        k -= 1

    return result
