import os
from enum import Enum
from collections import deque

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

class NormalAxis(Enum):
  X_POS = 1
  X_NEG = 2
  Y_POS = 3
  Y_NEG = 4
  Z_POS = 5
  Z_NEG = 6

exposed_sides = set()
max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')
min_x, min_y, min_z = float('inf'), float('inf'), float('inf')
for l in f:
  x, y, z = l.strip().split(',')
  x, y, z = int(x), int(y), int(z)
  max_x = max(max_x, x)
  min_x = min(min_x, x)
  max_y = max(max_y, y)
  min_y = min(min_y, y)
  max_z = max(max_z, z)
  min_z = min(min_z, z)

  if (x + 1, y, z, NormalAxis.X_NEG) in exposed_sides:
    exposed_sides.remove((x + 1, y, z, NormalAxis.X_NEG))
  else:
    exposed_sides.add((x, y, z, NormalAxis.X_POS))
  if (x - 1, y, z, NormalAxis.X_POS) in exposed_sides:
    exposed_sides.remove(((x - 1, y, z, NormalAxis.X_POS)))
  else:
    exposed_sides.add((x, y, z, NormalAxis.X_NEG))

  if (x, y + 1, z, NormalAxis.Y_NEG) in exposed_sides:
    exposed_sides.remove((x, y + 1, z, NormalAxis.Y_NEG))
  else:
    exposed_sides.add((x, y, z, NormalAxis.Y_POS))
  if (x, y - 1, z, NormalAxis.Y_POS) in exposed_sides:
    exposed_sides.remove((x, y - 1, z, NormalAxis.Y_POS))
  else:
    exposed_sides.add((x, y, z, NormalAxis.Y_NEG))

  if (x, y, z + 1, NormalAxis.Z_NEG) in exposed_sides:
    exposed_sides.remove((x, y, z + 1, NormalAxis.Z_NEG))
  else:
    exposed_sides.add((x, y, z, NormalAxis.Z_POS))
  if (x, y, z - 1, NormalAxis.Z_POS) in exposed_sides:
    exposed_sides.remove((x, y, z - 1, NormalAxis.Z_POS))
  else:
    exposed_sides.add((x, y, z, NormalAxis.Z_NEG))

max_x += 1
min_x -= 1
max_y += 1
min_y -= 1
max_z += 1
min_z -= 1

externally_exposed_sides = set()
q = deque([(max_x, max_y, max_z)])
added = set()
while q:
  x, y, z = q.popleft()
  for (n_x, n_y, n_z, norm) in [(x + 1, y, z, NormalAxis.X_NEG),
                                (x - 1, y, z, NormalAxis.X_POS),
                                (x, y + 1, z, NormalAxis.Y_NEG),
                                (x, y - 1, z, NormalAxis.Y_POS),
                                (x, y, z + 1, NormalAxis.Z_NEG),
                                (x, y, z - 1, NormalAxis.Z_POS)]:
    if (min_x <= n_x <= max_x) and (min_y <= n_y <= max_y) and (min_z <= n_z <=
                                                                max_z):
      if (n_x, n_y, n_z, norm) in exposed_sides:
        externally_exposed_sides.add((n_x, n_y, n_z, norm))
      elif (n_x, n_y, n_z) not in added:
        q.append((n_x, n_y, n_z))
        added.add((n_x, n_y, n_z))

# answer: 2468
print(len(externally_exposed_sides))
