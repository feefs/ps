import os
from enum import Enum

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

class NormalAxis(Enum):
  X_POS = 1
  X_NEG = 2
  Y_POS = 3
  Y_NEG = 4
  Z_POS = 5
  Z_NEG = 6

exposed_sides = set()
for l in f:
  x, y, z = l.strip().split(',')
  x, y, z = int(x), int(y), int(z)
  coord = (x, y, z)

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

# answer: 4340
print(len(exposed_sides))
