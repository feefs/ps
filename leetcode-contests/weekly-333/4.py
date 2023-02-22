# 2573. Find the String with LCP
class Solution:
  def findTheString(self, lcp: List[List[int]]) -> str:
    """
    key observation
      lcp[i][j] > 0 => result[i] == result[j]
        if lcp[i][j] is non-zero, then the corresponding characters in the result must be the same
      contrapositive of above statement: result[i] != result[j] => lcp[i][j] == 0
    valid lcp matrix property:
      if lcp[i][j] > 0, then lcp[i + 1][j + 1] must be equal to lcp[i][j] - 1 or 1 otherwise
    construct a string using the key observation, then check the contrapositive and valid lcp matrix property
    """
    n = len(lcp)
    # construct a string using the key observation
    characters = string.ascii_lowercase
    char_index = 0
    result = [False for _ in range(n)]
    for i in range(n):
      # skip result[i] if it's already set
      if result[i]:
        continue
      # try to set result[i], if we're out of characters it's impossible
      if char_index == 26:
        return ""
      result[i] = characters[char_index]
      for j in range(i + 1, n):
        # apply observation lcp[i][j] > 0 => result[i] == result[j]
        if lcp[i][j] > 0:
          result[j] = characters[char_index]
      char_index += 1

    for i in range(n):
      for j in range(n):
        if result[i] == result[j]:
          # validate lcp matrix property
          if i + 1 < n and j + 1 < n:
            if lcp[i][j] != 1 + lcp[i + 1][j + 1]:
              return ""
          else:
            if lcp[i][j] != 1:
              return ""
        else:
          # check contrapositive result[i] != result[j] => lcp[i][j] == 0
          if lcp[i][j] != 0:
            return ""

    return "".join(result)
