# 2598. Smallest Missing Non-negative Integer After Operations
class Solution:
  def findSmallestInteger(self, nums: List[int], value: int) -> int:
    """
    for any number in n, we can add/subtract value until it is n mod value
    count how many of each n mod value there are
    try to construct longest sequence using n mod value counts
    0 1 2 3
    [       ] 4 5 6          (1 2 3 mod 4)
            [       ] 7 8 X  (1 2 mod 4)
                    [       ]
    running out of 3 mod 4 in the 3rd round => mex is 9
    """
    mod_values = defaultdict(int)
    for n in nums:
      mod_values[n % value] += 1
    mex = 0
    while True:
      for v in range(value):
        if mod_values[v] == 0:
          return mex
        else:
          mod_values[v] -= 1
          mex += 1
