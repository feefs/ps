# 2751. Robot Collisions
class Solution:
  def survivedRobotsHealths(self, positions: List[int], healths: List[int],
                            directions: str) -> List[int]:
    """
    similar to 735. Asteroid Collision
    for each robot sorted by positions left to right
      iterate through the stack right to left and compute collisions
      add the robot to the stack if it survives
    """
    robots = zip(positions, healths, directions, range(1, len(positions) + 1))
    robots = [list(robot) for robot in robots]

    stack = []
    for pos, hp, d, idx in sorted(robots, key=lambda robot: robot[0]):
      if d == 'R':
        stack.append([pos, hp, d, idx])
      else:
        add_r = True
        # iterate through the stack from right to left and compute collisions
        while stack:
          # if the rightmost robot's direction is L, there will be no collision
          if stack[-1][2] == 'L':
            break
          # compare the current robot's hp to the rightmost robot's hp
          if hp > stack[-1][1]:
            stack.pop()
            hp -= 1
          elif hp == stack[-1][1]:
            stack.pop()
            add_r = False
            break
          else:
            add_r = False
            stack[-1][1] -= 1
            break
        if add_r:
          stack.append([pos, hp, d, idx])

    return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]
