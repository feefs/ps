# 2571. Minimum Operations to Reduce an Integer to 0
class Solution:
  def minOperations(self, n: int) -> int:
    """
    convert the number to binary
    for any number of consecutive ones, we can always add a number to save on operations
      0111 (add ->) 1000 (sub ->) 0000
      0111 (sub ->) 0011 (sub ->) 0001 (sub ->) 0000
    for two consecutive ones, adding and subtracting is the same number of operations
      011 (add ->) 100 (sub ->) 000
      011 (sub ->) 001 (sub ->) 000
      therefore, always try to add a number to potentially create more consecutive ones
        10011011 (add ->) 10011100 (add ->) 10100000 (sub ->) 00100000 (sub ->) 00000000
    edge case where adding a number leads to a bit larger than the original most significant bit
      11 (add ->) (1)00 (sub ->) (0)00
      instead of adding another bit, handle it implicitly by incrementing the sub_ops count
    after adding numbers, count the number of bits to subtract and add to add_ops
    """
    bin_string = list(bin(n)[2:])
    add_ops, sub_ops = 0, 0
    r = len(bin_string) - 1
    while r >= 0:
      if bin_string[r] == '0':
        r -= 1
        continue
      # treat r (right) index as inclusive and l (left) index as exclusive
      l = r - 1
      # expand l as much as we can
      while l >= 0 and bin_string[l] == '1':
        l -= 1
      # bin_string[l + 1:r + 1] will contain all ones at this point
      if r - l > 1:
        # add a number and turn the consecutive ones to zeros
        add_ops += 1
        for i in range(l + 1, r + 1):
          bin_string[i] = '0'
        # handle edge case by incrementing sub_ops instead of inserting another 1
        if l == -1:
          sub_ops += 1
        else:
          bin_string[l] = '1'
      r = l
    # count bits to subtract
    for b in bin_string:
      if b == '1':
        sub_ops += 1

    return add_ops + sub_ops
