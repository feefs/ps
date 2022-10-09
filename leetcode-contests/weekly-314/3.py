# 2434. Using a Robot to Print the Lexicographically Smallest String
class Solution:
  def robotWithString(self, s: str) -> str:
    t_stack = []
    s_q = deque(s)
    # used to quickly tell if a character is in s_q
    s_counts = {}
    for c in s:
      s_counts[c] = s_counts.get(c, 0) + 1

    result = []
    # greedily iterate through letters from lowest to highest
    for c in string.ascii_lowercase:
      # do the second action until the "end" of t is after c
      while t_stack and t_stack[-1] <= c:
        result.append(t_stack.pop())

      # at this point, the rest of s (s_q) might contain the letter c we are greedily looking for
      while c in s_counts:
        s_c = s_q.popleft()

        # update s_counts
        s_counts[s_c] -= 1
        if s_counts[s_c] == 0:
          del s_counts[s_c]

        if s_c == c:
          # do the first action + second action
          result.append(s_c)
        else:
          # do the first action, which may add characters less than a future c to t
          # this is why we pop <= c at the beginning of the loop
          t_stack.append(s_c)

    return "".join(result)
