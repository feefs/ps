# 2570. Merge Two 2D Arrays by Summing Values
class Solution:
  def mergeArrays(self, nums1: List[List[int]],
                  nums2: List[List[int]]) -> List[List[int]]:
    result = []
    i, j = 0, 0
    n1, n2 = len(nums1), len(nums2)
    while i < n1 and j < n2:
      id1, v1 = nums1[i]
      id2, v2 = nums2[j]
      if id1 == id2:
        result.append([id1, v1 + v2])
        i += 1
        j += 1
      elif id1 < id2:
        result.append([id1, v1])
        i += 1
      else:
        result.append([id2, v2])
        j += 1
    while i < n1:
      id1, v1 = nums1[i]
      result.append([id1, v1])
      i += 1
    while j < n2:
      id2, v2 = nums2[j]
      result.append([id2, v2])
      j += 1

    return result
