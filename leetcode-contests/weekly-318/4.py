# 2463. Minimum Total Distance Traveled
class Solution:
  def minimumTotalDistance(self, robot: List[int],
                           factory: List[List[int]]) -> int:
    """
    O(RFL) DP
    R = length of robot
    F = length of factory
    L = largest limit of a factory
    sort robot and factory
    f(rob_i, fac_j) = min cost to repair robots robot[rob_i:] with factories factory[fac_j:]
    """
    robot.sort()
    factory.sort()

    @cache
    def f(rob_i, fac_j):
      # no robots left to repair
      if rob_i == len(robot):
        return 0
      # no factories left to repair robots with
      if fac_j == len(factory):
        return float('inf')

      fac_pos, fac_lim = factory[fac_j]
      # cost so far
      cost = 0
      # default value for result is skipping this factory
      result = f(rob_i, fac_j + 1)
      for k in range(rob_i, min(rob_i + fac_lim, len(robot))):
        # repair a robot
        cost += abs(fac_pos - robot[k])
        # compute the cost to repair the rest of the robots with the rest of the factories
        result = min(result, cost + f(k + 1, fac_j + 1))
      return result

    return f(0, 0)
