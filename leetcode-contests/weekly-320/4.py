# 2478. Number of Beautiful Partitions
class Solution:
  def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
    """
    compute "blocks", partitions that start with a prime and end with a non-prime
      blocks are not guaranteed to be larger than minLength
    dp[i][q] = # of ways to beautifully partition blocks[i:] into q pieces all >= minLength
    """
    prime = set(['2', '3', '5', '7'])
    is_prime = lambda n: n in prime

    if not is_prime(s[0]) or is_prime(s[-1]):
      return 0

    blocks = []
    curr_size = 0
    for i in range(len(s) - 1):
      curr_size += 1
      if not is_prime(s[i]) and is_prime(s[i + 1]):
        blocks.append(curr_size)
        curr_size = 0
    blocks.append(curr_size + 1)

    B = len(blocks)

    # let j = next_block_index[i]
    # j = leftmost index where sum(block[i:j]) >= minLength, -1 if it doesn't exist
    # this is the leftmost index we can use dp subproblems for from the end
    next_block_index = [-1 for _ in range(B)]
    r = 0
    curr_size = 0
    for l in range(B):
      while r < B and curr_size < minLength:
        curr_size += blocks[r]
        r += 1
      if curr_size >= minLength:
        next_block_index[l] = r
      curr_size -= blocks[l]

    # dp[i][q] = # of ways to beautifully partition blocks[i:] into q pieces all >= minLength
    dp = [[0 for _ in range(k + 1)] for _ in range(B + 1)]
    dp[B][0] = 1

    # dp[i][q] = dp[i + 1][q - 1] + dp[i + 2][q - 1] + ... + dp[B - 1][q - 1]
    # (first term in equation above) dp[i + 1][q - 1] = dp[i + 2][q - 2] + dp[i + 3][q - 2] + ... + dp[B - 1][q - 2]
    # bottom up DP; q forwards from 1 to k, i backwards from B - 1 to 0
    # reuse results with total to reduce one dp dimension
    for q in range(k + 1):
      total = 0
      j = B
      for i in reversed(range(B)):
        if next_block_index[i] == -1:
          continue
        while j >= next_block_index[i]:
          total += dp[j][q - 1]
          total %= int(1e9) + 7
          j -= 1
        dp[i][q] = total

    return dp[0][k]
