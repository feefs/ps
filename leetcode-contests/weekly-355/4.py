# 2791. Count Paths That Can Form a Palindrome in a Tree
class Solution:
  def countPalindromePaths(self, parent: List[int], s: str) -> int:
    """
    given a path and the frequency counts of letters on it
      if at most one frequency is odd, a palindrome can be formed
    frequency count of (u, v) is the same as (u, root) + (v, root)
    use a 26 bit number to store the parity of character counts
    """
    # freq_parity returns the character frequency counts of (node, root) as a 26 bit number
    @cache
    def freq_parity(node):
      if node == 0:
        return 0
      curr_bit = (1 << ord(s[node]) - ord('a'))
      return freq_parity(parent[node]) ^ curr_bit

    counts = defaultdict(int)
    result = 0
    for node in range(len(parent)):
      parity = freq_parity(node)
      result += counts[parity]
      """
      increment result by the number of paths that can connect to (node, root) and form a palindrome
      a previous path works if it differs by at most one bit
        (prev, root) ^ (node, root) = parity of differing values
        => (prev, root) characters cancel with (node, root) characters to form a palindrome
        palindrome can be formed if at most one frequency is odd => can differ by at most one bit
      look for all paths that differ by at most one bit
      """
      result += sum(counts[parity ^ (1 << b)] for b in range(26))
      counts[parity] += 1

    return result
