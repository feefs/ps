import os
import re

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def manhattan_distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

intervals = []
for l in f:
  value = re.findall(r"=(-?\d+)", l.strip())
  sensor_x, sensor_y, beacon_x, beacon_y = value
  sensor_x, sensor_y = int(sensor_x), int(sensor_y)
  beacon_x, beacon_y = int(beacon_x), int(beacon_y)

  distance = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
  distance_at_target_height = manhattan_distance(sensor_x, sensor_y, sensor_x,
                                                 2_000_000)
  if distance_at_target_height <= distance:
    l = sensor_x - (distance - distance_at_target_height)
    r = sensor_x + (distance - distance_at_target_height)
    intervals.append([l, r])

intervals.sort()

merged_intervals = []
current_interval = intervals[0]
for interval in intervals[1:]:
  if interval[0] <= current_interval[1]:
    current_interval[1] = max(current_interval[1], interval[1])
  else:
    merged_intervals.append(current_interval)
    current_interval = interval
merged_intervals.append(current_interval)

# answer: 5142231
print(sum([i[1] - i[0] for i in merged_intervals]))
