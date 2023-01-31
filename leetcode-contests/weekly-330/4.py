# 2552. Count Increasing Quadruplets
class Solution:
  def countQuadruplets(self, nums: List[int]) -> int:
    N = len(nums)
    # less[n - 1][j] = number of elements in nums[:j] that are less than n
    less = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(1, N + 1):
      i = n - 1
      for j in range(1, N):
        less[i][j] = less[i][j - 1] + (1 if nums[j - 1] < n else 0)

    result = 0
    for j in range(N):
      for k in range(j + 1, N):
        num_j, num_k = nums[j], nums[k]
        if num_k < num_j:
          """
          compute total values > num_j in nums[k + 1:]
          (total values > num_j) - (total values > num_j in nums[:k])
            total values > num_j = N - num_j, since the array contains 1 - n
            total values > num_j in nums[:k] = slots - (total values < num_j in nums[:k])
              slots = k - 1, since one is occupied by num_j at j (j < k is guaranteed)
              total values < num_j in nums[:k] = less[num_j - 1][k]
          => (N - num_j) - ((k - 1) - less[num_j - 1][k])
          """
          result += less[num_k - 1][j] * ((N - num_j) -
                                          ((k - 1) - less[num_j - 1][k]))

    return result

  def countQuadruplets(self, nums: List[int]) -> int:
    """
    TLE
    Compute DP twice
    """
    N = len(nums)
    # less[n - 1][j] = number of elements in nums[:j] that are less than n
    # more[n - 1][j] = number of elements in nums[j + 1:] that are less than n
    less = [[0 for _ in range(N)] for _ in range(N)]
    more = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(1, N + 1):
      i = n - 1
      for j in range(1, N):
        less[i][j] = less[i][j - 1] + (1 if nums[j - 1] < n else 0)
      for j in reversed(range(N - 1)):
        more[i][j] = more[i][j + 1] + (1 if nums[j + 1] > n else 0)

    result = 0
    for j in range(N):
      for k in range(j + 1, N):
        num_j, num_k = nums[j], nums[k]
        if num_k < num_j:
          # i < j < k < l and nums[i] < nums[k] < nums[j] < nums[l]
          # => find # of values less than num_k and before index j
          # => find # of values greater than num_j and after index k
          result += less[num_k - 1][j] * more[num_j - 1][k]

    return result
