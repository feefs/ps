# 2736. Maximum Sum Queries
class Solution:
  def maximumSumQueries(self, nums1: List[int], nums2: List[int],
                        queries: List[List[int]]) -> List[int]:
    """
    interpret nums1 and nums2 as a list of points
    build a valid list of (y, x + y) values
      left to right monotonically increasing y to enable binary search
      left to right monotonically decreasing (x + y) values to guarantee the best value
    iterate through queries in decreasing x value order
      work through points in decreasing x value order, save work each iteration
        update valid list
      binary search for a valid y value to answer the query
    """
    sorted_points = sorted(zip(nums1, nums2), reverse=True)
    result = [0 for _ in range(len(queries))]
    largest_y = 0
    valid = []
    i = 0
    for q_i, (x, y) in sorted(enumerate(queries),
                              key=lambda p: p[1][0],
                              reverse=True):
      while i < len(sorted_points) and sorted_points[i][0] >= x:
        """
        if the current point's y is smaller than largest_y, a better point already exists in valid
          larger y value (less restrictive)
          better x + y value
            since we iterate from larger to smaller x values, better x >= current x
            since largest_y > y, better y > current y
            => better point's x + y >= current point's x + y
        """
        if sorted_points[i][1] > largest_y:
          largest_y = sorted_points[i][1]
          """
          current y, now largest_y, may have a larger (x + y) value than points in valid
          pop off points in valid with smaller (x + y) values (keep monotonically decreasing x + y values)
            this is correct because current y is now largest_y
              current y is now the least restrictive y value
              current y is now the largest, so appending still keeps monotonically increasing y values
          """
          while valid and valid[-1][
              1] < sorted_points[i][0] + sorted_points[i][1]:
            valid.pop()
          valid.append((largest_y, sorted_points[i][0] + sorted_points[i][1]))
        i += 1
      # binary search valid using the y value, and set the query response to (x + y)
      valid_i = bisect_left(valid, (y, 0))
      result[q_i] = valid[valid_i][1] if valid_i < len(valid) else -1

    return result
