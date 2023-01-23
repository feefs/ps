# 2545. Sort the Students by Their Kth Score
class Solution:
  def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
    """
    python 1-liner
    """
    return sorted(score, key=lambda row: row[k], reverse=True)

  def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
    """
    dictionary approach
    """
    index_to_row = {i: row for i, row in enumerate(score)}
    row_pairs = [(i, row[k]) for i, row in enumerate(score)]
    row_pairs.sort(key=lambda p: p[1])

    return [index_to_row[i] for i, _ in reversed(row_pairs)]
