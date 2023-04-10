# 2614. Prime In Diagonal
class Solution:
  def diagonalPrime(self, nums: List[List[int]]) -> int:
    # prime number sieve
    N = len(nums)
    largest = max([nums[i][i]
                   for i in range(N)] + [nums[i][N - i - 1] for i in range(N)])
    sieve = [True for _ in range(largest + 1)]
    n = 2
    while n**2 <= largest:
      if sieve[n]:
        for c in range(n * 2, largest + 1, n):
          sieve[c] = False
      n += 1
    primes = set()
    for n in range(2, largest + 1):
      if sieve[n]:
        primes.add(n)

    N = len(nums)
    result = 0
    for i in range(N):
      if nums[i][i] in primes:
        result = max(result, nums[i][i])
      if nums[i][N - i - 1] in primes:
        result = max(result, nums[i][N - i - 1])

    return result
