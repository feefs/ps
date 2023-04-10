# 2615. Sum of Distances
class Solution:
  def distance(self, nums: List[int]) -> List[int]:
    """
    group indices with the same values into buckets
    for each bucket, iterate over its values
      for each value, compute its sum of distances
        since each bucket's values are monotonically increasing, use a prefix sum
        compute sum of distances before and after the value separately
          rearrange |i - j| equation
            group all i values into (v * prev_n)/(v * post_n)
            group all j values into prev_sum/post_sum
        set the corresponding number in result to the sum of distances for the value
    """
    buckets = defaultdict(list)
    for i, n in enumerate(nums):
      buckets[n].append(i)

    result = [0 for _ in range(len(nums))]
    for bucket in buckets.values():
      # pre[bucket_i] = sum(bucket[:bucket_i + 1])
      pre = []
      curr = 0
      for v in bucket:
        curr += v
        pre.append(curr)
      for bucket_i, v in enumerate(bucket):
        # number of elements before and after bucket_i
        prev_n, post_n = bucket_i, len(bucket) - bucket_i - 1
        # sum of elements before and after bucket_i
        prev_sum, post_sum = pre[bucket_i] - v, pre[-1] - pre[bucket_i]
        result[v] = ((v * prev_n) - prev_sum) + (post_sum - (v * post_n))

    return result
