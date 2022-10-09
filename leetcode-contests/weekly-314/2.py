# 2433. Find The Original Array of Prefix Xor
class Solution:
  def findArray(self, pref: List[int]) -> List[int]:
    result = [pref[0]]

    # result[i] = pref[i] ^ (arr[0] ^ ... ^ arr[i - 1]) = pref[i] ^ (pref[i - 1])
    for i in range(1, len(pref)):
      n = pref[i]
      result.append(n ^ pref[i - 1])

    return result
