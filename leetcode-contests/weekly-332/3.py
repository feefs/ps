# 2564. Substring XOR Queries
class Solution:
  def substringXorQueries(self, s: str,
                          queries: List[List[int]]) -> List[List[int]]:
    N = len(s)
    values = defaultdict(lambda: [-1, -1])
    for i in range(N):
      # instead of range(i, N), we can limit it to i + 30 since log_2(10^9) is 29.9
      for j in range(i, i + 30):
        # print((i, j), s[i:j + 1], int(s[i:j + 1], 2))
        subs = s[i:j + 1]
        # continue if leading zero
        if subs[0] == '0' and len(subs) > 1:
          continue
        v = int(subs, 2)
        if v not in values:
          values[v] = (i, j)

    return [values[q[0] ^ q[1]] for q in queries]
