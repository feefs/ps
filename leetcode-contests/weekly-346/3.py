# 2698. Find the Punishment Number of an Integer
class Solution:
  def punishmentNumber(self, n: int) -> int:
    @cache
    def can_make(s, target):
      if int(s) == target:
        return True
      for i in range(1, len(s)):
        if can_make(s[i:], target - int(s[:i])):
          return True
      return False

    result = 0
    for i in range(1, n + 1):
      if can_make(str(i * i), i):
        result += i * i

    return result
