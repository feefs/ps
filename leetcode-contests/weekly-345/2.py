# 2683. Neighboring Bitwise XOR
class Solution:
  def doesValidArrayExist(self, derived: List[int]) -> bool:
    """
    fix starting value to 0 or 1 and test if a valid binary array is possible
    og[0] = starting value
    rearrange equation og[i] ^ og[i + 1] = d[i]
      => og[i + 1] = d[i] ^ og[i]
    last index is -1, og[-1] ^ og[0] = d[-1]
      => og[0] = d[-1] ^ og[-1]
      => starting value = d[-1] ^ og[-1]
    compute og[-1] by keeping a running xor
      if starting value == d[-1] ^ og[-1], the binary array is possible
    """
    value = 0
    for d in derived:
      value ^= d
    if value == 0:
      return True
    value = 1
    for d in derived:
      value ^= d
    if value == 1:
      return True

    return False
