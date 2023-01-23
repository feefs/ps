# 2546. Apply Bitwise Operations to Make Strings Equal
class Solution:
  def makeStringsEqual(self, s: str, target: str) -> bool:
    """
    for any (i, j),
      (0, 0) can only turn into (0, 0)
      (1, 0) can turn into (1, 1)
      (0, 1) can turn into (1, 1)
      (1, 1) can turn into (1, 0) or (0, 1)
    if there are no 1s in s and no 1s in target
      return True since both strings are all 0s
    if there are 1s in s and no 1s in target
      return False since we can't remove all 1s in s
        we need to pick different indices for i and j
    if there are no 1s in s but 1s in target, we can't
      return False since we can't add any 1s in s
    if there are 1s in s and 1s in target
      return True since we can always add or remove zeros to match target
    """
    no_ones_in_s = s.count("1") == 0
    no_ones_in_target = target.count("1") == 0
    return no_ones_in_s == no_ones_in_target
