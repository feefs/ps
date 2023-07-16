# 2781. Length of the Longest Valid Substring
class Solution:
  def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
    """
    after adding a character word[r], check all substrings left to right that include the new character
      since forbidden[i].length <= 10, we only need to check starting from 10 characters back
    keep track of left, the index of a valid substring that ends at the current character word[r]
      move it forward if a forbidden substring is encountered
    """
    forbidden = set(forbidden)
    result = 0
    left = 0
    for r in range(len(word)):
      for l in range(max(left, r - 10), r + 1):
        if word[l:r + 1] in forbidden:
          left = l + 1
      result = max(result, r - left + 1)

    return result
