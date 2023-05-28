# 2713. Maximum Strictly Increasing Cells in a Matrix
class Solution:
  def maxIncreasingCells(self, mat: List[List[int]]) -> int:
    """
    place values into an empty grid in decreasing order
      this guarantees we will always be able to move from the current cell to previously placed values
    compute longest path achievable from the current cell
      1 + the longest path achievable from another cell in the current row and column
      update the longest path achievable from the current cell's row and column
    """
    m, n = len(mat), len(mat[0])
    coordinates = defaultdict(list)
    for i in range(m):
      for j in range(n):
        coordinates[mat[i][j]].append((i, j))

    grid = [[0 for _ in range(n)] for _ in range(m)]
    row_max_paths, col_max_paths = [0 for _ in range(m)], [0 for _ in range(n)]
    for _, coords in reversed(sorted(coordinates.items())):
      for i, j in coords:
        grid[i][j] = 1 + max(row_max_paths[i], col_max_paths[j])
      # batch update the longest path achievable from the cell's row and column for all cells with the same value
      # this avoids treating another cell with the same value as reachable
      for i, j in coords:
        longest_path = max([grid[i][j] for i, j in coords])
        row_max_paths[i] = max(row_max_paths[i], grid[i][j])
        col_max_paths[j] = max(col_max_paths[j], grid[i][j])

    result = 0
    for i in range(m):
      for j in range(n):
        result = max(result, grid[i][j])

    return result
