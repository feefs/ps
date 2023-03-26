# 2601. Prime Subtraction Operation
class Solution:
  def primeSubOperation(self, nums: List[int]) -> bool:
    # prime number sieve
    largest = max(nums)
    sieve = [True for _ in range(largest + 1)]
    n = 2
    while n**2 <= largest:
      if sieve[n]:
        for c in range(n**2, largest, n):
          sieve[c] = False
      n += 1
    primes = []
    n = 2
    while n <= largest:
      if sieve[n]:
        primes.append(n)
      n += 1

    # if n == 1 or n == 2, this will return None since there are no primes less than 1 or 2
    def largest_strictly_less_prime(n):
      l, r = 0, len(primes)
      while l < r:
        mid = (l + r) // 2
        if primes[mid] < n:
          l = mid + 1
        else:
          r = mid
      return primes[l - 1] if l > 0 else None

    """
    repeatedly check the current number n against the previous number prev
    if there exists a prime p such that n - p > prev
      we can subtract it from n while still keeping a strictly increasing order
      this can only make things better
    rearrange the equation to n - prev > p
      look for a prime p that's less than n - prev
    """
    prev = 0
    for i in range(len(nums)):
      p = largest_strictly_less_prime(nums[i] - prev)
      # if there exists a p that satisfies n - prev > p, subtract it from n
      if p:
        nums[i] -= p
      if nums[i] <= prev:
        return False
      prev = nums[i]

    return True
