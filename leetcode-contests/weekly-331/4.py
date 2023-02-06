# 2561. Rearranging Fruits
class Solution:
  def minCost(self, basket1: List[int], basket2: List[int]) -> int:
    # if any count of numbers is odd, we cannot pair them up
    c = Counter(basket1 + basket2)
    for v in c.values():
      if v % 2 == 1:
        return -1

    # compute l1 and l2, the list of numbers that aren't in the other baskets
    # values in l1 and l2 represent number pairs in surplus for that respective list
    for v in basket2:
      # subtract 2 since values in basket2 were already counted once above
      c[v] -= 2
    surplus1, surplus2 = [], []
    for k, v in c.items():
      if v == 0:
        continue
      if v > 0:
        surplus1.extend([k for _ in range(v // 2)])
      else:
        surplus2.extend([k for _ in range(abs(v // 2))])
    l1, l2 = deque(sorted(surplus1)), deque(sorted(surplus2))

    cost = 0
    """
    for the min number pair in one list with value A and the max number pair in the other list with value B
      we can swap one A value with one B value for cost A
      we can also do an indirect swap by swapping twice with the smallest value for a potential lower cost
        smallest in same list as A => swap one B value with smallest, then swap A with that smallest value
        smallest in other list => swap one A value with smallest, then swap B value with that smallest value
          swapping this way will always keep smallest in its original list, not that it matters
    """
    indirect_swap_cost = 2 * min(min(basket1), min(basket2))
    while l1 and l2:
      # look at the front of l1 and l2 to determine which opposite number pairs to process, smaller will always be better
      # the pop statements only represent the number pairs with values A and B being processed, not what swaps happened
      if l1[0] < l2[0]:
        cost += min(l1[0], indirect_swap_cost)
        l1.popleft()
        l2.pop()
      else:
        cost += min(l2[0], indirect_swap_cost)
        l2.popleft()
        l1.pop()

    return cost
