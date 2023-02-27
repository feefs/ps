# 2575. Find the Divisibility Array of a String
class Solution:
  def divisibilityArray(self, word: str, m: int) -> List[int]:
    digits = [int(c) for c in word]
    result = []
    curr_num_mod_m = 0
    for d in digits:
      curr_num_mod_m = ((curr_num_mod_m * 10) + d) % m
      result.append(1 if curr_num_mod_m == 0 else 0)

    return result
