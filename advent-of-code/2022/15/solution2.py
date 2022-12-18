import os
import re

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def manhattan_distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

pos_line_intercepts = set()
neg_line_intercepts = set()
sensors = []
for l in f:
  value = re.findall(r"=(-?\d+)", l.strip())
  sx, sy, bx, by = value
  sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
  distance = manhattan_distance(sx, sy, bx, by)
  sensors.append([(sx, sy), manhattan_distance(sx, sy, bx, by)])
  # compute y intercepts of 4 perimeter lines (1 more than manhattan distance away)
  pos_line_intercepts.add((sy + distance + 1) - sx)
  pos_line_intercepts.add((sy - distance - 1) - sx)
  neg_line_intercepts.add((sy + distance + 1) + sx)
  neg_line_intercepts.add((sy - distance - 1) + sx)

intersections = []
for y1 in pos_line_intercepts:
  for y2 in neg_line_intercepts:
    # y = x + y1
    # y = -x + y2
    # => x + y1 = -x + y2 => 2x = y2 - y1 => x = (y2 - y1) / 2
    # plug x back in either of the two equations, y = (y1 + y2) / 2
    x = (y2 - y1) // 2
    y = (y1 + y2) // 2
    if 0 <= x <= 4_000_000 and 0 <= y <= 4_000_000:
      intersections.append((x, y))

# search for the intersection point of perimeter lines outside the range of all sensors
for x, y in intersections:
  is_outside_all = True
  for (sx, sy), distance in sensors:
    if manhattan_distance(x, y, sx, sy) <= distance:
      is_outside_all = False
  if is_outside_all:
    # answer: 10884459367718
    print((x * 4_000_000) + y)
    break
