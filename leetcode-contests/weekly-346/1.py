# 2696. Minimum String Length After Removing Substrings
class Solution:
  def minLength(self, s: str) -> int:
    stack = []
    removed = 0
    mappings = {'A': 'B', 'C': 'D'}
    for c in s:
      if c in mappings:
        stack.append(c)
      elif stack:
        if mappings[stack[-1]] == c:
          stack.pop()
          removed += 2
        else:
          stack.clear()

    return len(s) - removed
