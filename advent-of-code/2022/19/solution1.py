import os
import re

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def check_blueprint(r1_ore_cost, r2_ore_cost, r3_ore_cost, r3_clay_cost,
                    r4_ore_cost, r4_obs_cost):
  max_ore = max(r1_ore_cost, r2_ore_cost, r3_ore_cost, r4_ore_cost)
  max_clay = r3_clay_cost
  max_obsidian = r4_obs_cost
  cache = {}
  most_geodes = float('-inf')

  def dfs(time, robots, resources):
    nonlocal most_geodes

    r1, r2, r3, r4 = robots
    res1, res2, res3, res4 = resources

    if time == 0:
      most_geodes = max(most_geodes, res4)
      return res4

    key = (time, *robots, *resources)
    if key in cache:
      return cache[key]

    result = res4 + (r4 * time)

    if result + sum(range(time)) < most_geodes:
      cache[key] = result
      return result

    result = max(
        result,
        dfs(time - 1, robots, (res1 + r1, res2 + r2, res3 + r3, res4 + r4)))
    if r1 < max_ore and res1 >= r1_ore_cost:
      result = max(
          result,
          dfs(time - 1, (r1 + 1, r2, r3, r4),
              (res1 + r1 - r1_ore_cost, res2 + r2, res3 + r3, res4 + r4)))
    if r2 < max_clay and res1 >= r2_ore_cost:
      result = max(
          result,
          dfs(time - 1, (r1, r2 + 1, r3, r4),
              (res1 + r1 - r2_ore_cost, res2 + r2, res3 + r3, res4 + r4)))
    if r3 < max_obsidian and res1 >= r3_ore_cost and res2 >= r3_clay_cost:
      result = max(
          result,
          dfs(time - 1, (r1, r2, r3 + 1, r4),
              (res1 + r1 - r3_ore_cost, res2 + r2 - r3_clay_cost, res3 + r3,
               res4 + r4)))
    if res1 >= r4_ore_cost and res3 >= r4_obs_cost:
      result = max(
          result,
          dfs(time - 1, (r1, r2, r3, r4 + 1),
              (res1 + r1 - r4_ore_cost, res2 + r2, res3 + r3 - r4_obs_cost,
               res4 + r4)))

    cache[key] = result
    return result

  return dfs(24, (1, 0, 0, 0), (0, 0, 0, 0))

total_quality_levels = 0
for l in f:
  value = l.strip()
  blueprint_num = int(re.findall(r"Blueprint (\d+):", value)[0])
  r1_ore_cost = int(re.findall(r"Each ore robot costs (\d+) ore.", value)[0])
  r2_ore_cost = int(re.findall(r"Each clay robot costs (\d+) ore.", value)[0])

  obsidian_robot_cost = re.findall(
      r"Each obsidian robot costs (\d+) ore and (\d+) clay.", value)[0]
  r3_ore_cost, r3_clay_cost = (int(obsidian_robot_cost[0]),
                               int(obsidian_robot_cost[1]))

  geode_robot_cost = re.findall(
      r"Each geode robot costs (\d+) ore and (\d+) obsidian.", value)[0]
  r4_ore_cost, r4_obs_cost = (int(geode_robot_cost[0]),
                              int(geode_robot_cost[1]))

  print("BLUEPRINT:", blueprint_num)
  result = check_blueprint(r1_ore_cost, r2_ore_cost, r3_ore_cost, r3_clay_cost,
                           r4_ore_cost, r4_obs_cost)
  total_quality_levels += (blueprint_num * result)
  print("RESULT:", result)
  print()

# answer: 1613
print(total_quality_levels)
