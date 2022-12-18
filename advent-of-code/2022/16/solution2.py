import os
from collections import defaultdict
import re
import functools

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

flow = {}
children = defaultdict(set)
for l in f:
  valve, flow_rate, children_string = re.findall(
      r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)",
      l.strip())[0]
  flow[valve] = int(flow_rate)
  for c in children_string.split(', '):
    children[valve].add(c)

bit_mappings = {v: 1 << i for i, v in enumerate(flow.keys())}

@functools.lru_cache(maxsize=None)
def dfs(valve, time, opened, openers_left):
  if time <= 0:
    if openers_left > 0:
      return dfs('AA', 26, opened, 0)
    else:
      return 0
  result = 0
  if flow[valve] > 0 and opened & bit_mappings[valve] == 0:
    for c in children[valve]:
      result = max(result, ((time - 1) * flow[valve]) +
                   dfs(c, time - 2, opened | bit_mappings[valve], openers_left))
  for c in children[valve]:
    result = max(result, dfs(c, time - 1, opened, openers_left))
  return result

# answer: 2615
print(dfs('AA', 26, 0, 1))
