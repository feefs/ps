# 2719. Count of Integers
class Solution:
  def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    """
    digit dp, build and count numbers that are up to a value or digit sum
      iterate backwards to simplify parameters for @cache
      num_limit_index
        2 if we picked a lower digit for the previous, larger subproblem's more significant digit
          current less significant digit can be anything [1-9]
        0 or 1 if we didn't pick a lower digit for the previous, larger subproblem's more significant digit
          current less significant digit is limited by the current number's digit
            otherwise, the value would exceed the current number
    inclusion exclusion for num1 <= x <= num2 && min_sum <= digit_sum(x) <= max_sum
      x <= num2 && digit_sum(x) <= max_sum
        subtract out x <= num2 && min_sum < digit_sum(x)
        subtract out num1 < x && digit_sum(x) <= max_sum
        add back num1 < x && min_sum < digit_sum(x)
    """
    nums = (str(int(num1) - 1)[::-1], num2[::-1])

    @cache
    def f(i, num_limit_index, digit_sum_limit):
      if i == -1:
        return 1
      digits = 9
      # limit digit choices if a lower digit wasn't picked in the previous, larger subproblem
      if num_limit_index != 2:
        digits = int(nums[num_limit_index][i])
      result = 0
      for d in range(min(digits, digit_sum_limit) + 1):
        if d == digits:
          # pick the original digit, the next less significant digit will be limited
          result += f(i - 1, num_limit_index, digit_sum_limit - d)
        else:
          # pick a lower digit, the next less significant digit will not be limited
          result += f(i - 1, 2, digit_sum_limit - d)
      return result

    def g(num_index, digit_sum_limit):
      if num_index == 0:
        return f(len(num1) - 1, 0, digit_sum_limit)
      else:
        return f(len(num2) - 1, 1, digit_sum_limit)

    # inclusion exclusion
    return (g(1, max_sum) - g(1, min_sum - 1) - g(0, max_sum) +
            g(0, min_sum - 1)) % ((10**9) + 7)
