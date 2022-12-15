import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

space = set()
lowest_rock = 0

def add_segments(points):
  for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        space.add((x1, y))
    else:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        space.add((x, y1))

for l in f:
  value = l.strip()
  point_strings = value.split(" -> ")
  points = []
  for p in point_strings:
    l, r = p.split(',')
    points.append((int(l), int(r)))
    lowest_rock = max(lowest_rock, int(r))
  add_segments(points)

def drop_sand():
  x, y = 500, 0
  while y < lowest_rock:
    if (x, y + 1) not in space:
      y += 1
    elif (x - 1, y + 1) not in space:
      x -= 1
      y += 1
    elif (x + 1, y + 1) not in space:
      x += 1
      y += 1
    else:
      break
  if y >= lowest_rock:
    return False
  else:
    space.add((x, y))
    return True

settled_sand = 0
while drop_sand():
  settled_sand += 1

# answer: 1001
print(settled_sand)
