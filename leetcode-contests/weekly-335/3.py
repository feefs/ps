# 2584. Split the Array to Make Coprime Products
class Solution:
  def findValidSplit(self, nums: List[int]) -> int:
    """
    prime factorization
    compute intervals
      start and end are the first and last elements that are divisible by the prime number
    find split point that doesn't lie in any of the intervals
      [4  7  8  15 3  5] <- nums
    2  *-----*
    3           *--*
    5           *-----*
    7     *
    11
    13
    intervals[i] = how many intervals to open/close after processing nums[i]
      add one to intervals[i] to open an interval
      subtract one from intervals[i] to close an interval
      intervals from example above:
      [1  0  -1 2 -1 -1]
        once we reach index i = 2, there are 0 open intervals => split at i = 2
    start from i = 1 with intervals[0] open intervals
      if the number of open intervals drops to 0, we can split at i
      if the number of intervals doesn't drop to 0 before the end, we can't split
    """
    # prime number sieve
    largest = max(nums)
    sieve = [True for _ in range(largest + 1)]
    n = 2
    while n**2 <= largest:
      if sieve[n]:
        for c in range(n * 2, largest + 1, n):
          sieve[c] = False
      n += 1
    primes = []
    n = 2
    while n <= largest:
      if sieve[n]:
        primes.append(n)
      n += 1
    primes_set = set(primes)

    # compute prime interval bounds
    """
    optimization when finding all primes that divide a number n
      keep a running prime factorization (rpf) of n
      if the rpf is divisible by a prime p, divide p out of the rpf
      rpf is divisible by a prime p <=> n must be divisible by p
      halt early if a prime p2 ** 2 exceeds the rpf
        all previous primes have been tested and divided out of the rpf
        rpf = ((((n / 2) / 3) / ...) / p), where p is the prime before p2
        => only new primes we can try to divide out are primes >= p2:
          rpf / p2 = k * p2, rpf / p3 = k * p2, rpf / p4 = k * p2 where p2 < p3 < p4 ...
        if p2 ** 2 > rpf, then the rpf is not large enough to try primes >= p2
        => terminate early
      remaining rpf might be prime, set its bounds if that's the case
    """
    bounds = {}
    for i, n in enumerate(nums):
      rpf = n
      for p in primes:
        # optimization
        if p**2 > rpf:
          break
        if rpf % p == 0:
          if p not in bounds:
            bounds[p] = [i, i]
          bounds[p][1] = i
          # optimization
          rpf //= p
        # optimization
        if rpf > 1 and rpf in primes_set:
          if rpf not in bounds:
            bounds[rpf] = [i, i]
          bounds[rpf][1] = i

    # construct intervals
    intervals = [0 for _ in range(len(nums))]
    for _, (l, r) in bounds.items():
      intervals[l] += 1
      intervals[r] -= 1

    # find potential split point
    open_intervals = intervals[0]
    for i in range(1, len(intervals) - 1):
      open_intervals += intervals[i]
      if open_intervals == 0:
        return i

    # if no split point can be found, return -1
    return -1
