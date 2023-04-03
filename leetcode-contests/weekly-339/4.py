# 2612. Minimum Reverse Operations
from sortedcontainers import SortedList

class Solution:
  def minReverseOperations(self, n: int, p: int, banned: List[int],
                           k: int) -> List[int]:
    """
    observe a 1 at position i can only be moved in increments of 2
      even vs odd neighbors are determined by whether or not k is even or odd
    bfs starting from p
      for each position i, compute its neighbors
        leftmost and rightmost interval endpoints are i - (k - 1) and i + (k - 1)
          ensure these values are in bounds
        rightmost interval starts at (rightmost interval endpoint) - (k - 1) = (i + (k - 1)) - (k - 1)
        for an interval starting at start and ending at end = start + (k - 1)
          let pos be where the 1 is, where start <= x <= end
          the position where it's reversed to is start + (end - x)
        compute the leftmost neighbor and rightmost neighbor and perform a range query
          use sorted lists for logarithmic complexity operations
          prune neighbors when they are added to the queue to speed up future range queries
    """
    banned_set = set(banned)
    even, odd = SortedList(), SortedList()
    for i in range(n):
      if i != p and i not in banned_set:
        (even if i % 2 == 0 else odd).add(i)

    def reversed_position(interval_start, pos):
      interval_end = interval_start + (k - 1)
      return interval_start + (interval_end - pos)

    result = [-1 for _ in range(n)]
    q = deque([(p, 0)])
    while q:
      next_q = deque([])
      while q:
        i, steps = q.popleft()
        result[i] = steps
        # leftmost and rightmost interval endpoints
        l_int, r_int = max(0, i - (k - 1)), min(n - 1, i + (k - 1))
        # leftmost and rightmost starting interval points
        lo, hi = l_int, r_int - (k - 1)
        # leftmost and rightmost neighbor values from reversing subarrays
        l_neb, r_neb = reversed_position(lo, i), reversed_position(hi, i)
        to_prune = []
        neighbors = (even if l_neb % 2 == 0 else odd)
        for neb_i in range(neighbors.bisect_left(l_neb),
                           neighbors.bisect_right(r_neb)):
          next_q.append((neighbors[neb_i], steps + 1))
          to_prune.append(neighbors[neb_i])
          neb_i += 1
        # prune added neighbors
        for neb in to_prune:
          neighbors.remove(neb)
      q = next_q

    return result

  def minReverseOperations(self, n: int, p: int, banned: List[int],
                           k: int) -> List[int]:
    """
    TLE
    Compute full range of possible moves
    """
    banned_set = set(banned)

    def possible_moves(i):
      leftmost_endpoint = max(0, i - (k - 1))
      rightmost_endpoint = min(n - 1, i + (k - 1))
      lo, hi = leftmost_endpoint, rightmost_endpoint - (k - 1)
      result = []
      for start in range(lo, hi + 1):
        end = start + (k - 1)
        pos = start + (end - i)
        if pos not in banned:
          result.append(pos)
      return result

    result = [-1 for _ in range(n)]
    added = {p}
    q = deque([(p, 0)])
    while q:
      next_q = deque([])
      while q:
        i, steps = q.popleft()
        result[i] = steps
        for move in possible_moves(i):
          if move not in added:
            added.add(move)
            next_q.append((move, steps + 1))
      q = next_q

    return result
