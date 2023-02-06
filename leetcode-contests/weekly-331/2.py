# 2559. Count Vowel Strings in Ranges
class Solution:
  def vowelStrings(self, words: List[str],
                   queries: List[List[int]]) -> List[int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # left[i] = number of words before index i that start and end with a vowel
    # right[i] = number of words after index i that start and end with a vowel
    left = []
    curr = 0
    for w in words:
      left.append(curr)
      if w[0] in vowels and w[-1] in vowels:
        curr += 1
    right = []
    curr = 0
    for w in reversed(words):
      right.insert(0, curr)
      if w[0] in vowels and w[-1] in vowels:
        curr += 1
    total = curr

    return [total - left[l] - right[r] for l, r in queries]
