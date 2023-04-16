# 2645. Minimum Additions to Make Valid String
class Solution:
  def addMinimum(self, word: str) -> int:
    n = len(word)
    result = 0
    # two letter strings that can be made valid by inserting one character
    twos = set(['ab', 'bc', 'ac'])
    i = 0
    # invariant: word[:i] has already been processed to form a valid string
    while i < n:
      if word[i:i + 3] == 'abc':
        i += 3
      elif word[i:i + 2] in twos:
        result += 1
        i += 2
      else:
        result += 2
        i += 1

    return result
