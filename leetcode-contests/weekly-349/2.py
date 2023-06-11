# 2734. Lexicographically Smallest String After Substring Operation
class Solution:
  def smallestString(self, s: str) -> str:
    n = len(s)
    mapping = {
        c: r
        for c, r in zip(string.ascii_lowercase, ['z'] +
                        list(string.ascii_lowercase[:-1]))
    }
    start = False
    result = list(s)

    for i, c in enumerate(s):
      if i == n - 1 and c == 'a' and not start:
        result[i] = mapping[c]
      if start:
        if c != 'a':
          result[i] = mapping[c]
        else:
          break
      else:
        if c != 'a':
          start = True
          result[i] = mapping[c]

    return "".join(result)
