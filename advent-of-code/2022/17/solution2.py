import os
import itertools
"""
Search for a cycle while dropping rocks
Map (rock_number, jet_index) to (step, height)
For a cache value with the same rock number and jet_index
  If the # of steps left is divisible by # of steps between the current step and the previous step
  => We can repeat the # of steps between the current step and the previous step until the end
  => Compute the height gained by multiplying the height difference by the number of cycles left
"""

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

jet_patterns = f.read().strip()
rock_numbers = itertools.cycle([1, 2, 3, 4, 5])

class Rock():
  def __init__(self, num, h):
    if num == 1:
      self.points = set([
          (2, h + 4),
          (3, h + 4),
          (4, h + 4),
          (5, h + 4),
      ])
    elif num == 2:
      self.points = {(2, h + 5), (3, h + 6), (3, h + 5), (3, h + 4), (4, h + 5)}
    elif num == 3:
      self.points = {(2, h + 4), (3, h + 4), (4, h + 6), (4, h + 5), (4, h + 4)}
    elif num == 4:
      self.points = {
          (2, h + 7),
          (2, h + 6),
          (2, h + 5),
          (2, h + 4),
      }
    else:
      self.points = {(2, h + 5), (2, h + 4), (3, h + 5), (3, h + 4)}

  def pushLeft(self, occupied):
    shifted_points = set([(p[0] - 1, p[1]) for p in self.points])
    for x, y in shifted_points:
      if x < 0 or (x, y) in occupied:
        return
    self.points = shifted_points

  def pushRight(self, occupied):
    shifted_points = set([(p[0] + 1, p[1]) for p in self.points])
    for x, y in shifted_points:
      if x > 6 or (x, y) in occupied:
        return
    self.points = shifted_points

  def fall(self, occupied):
    shifted_points = set([(p[0], p[1] - 1) for p in self.points])
    for x, y in shifted_points:
      if y == 0 or (x, y) in occupied:
        return True
    self.points = shifted_points
    return False

  def highest(self):
    return max(self.points, key=lambda p: p[1])[1]

height = 0
jet_index = 0
graph = set()
cache = {}
for step in range(1_000_000_000_000):
  rock_num = next(rock_numbers)
  rock = Rock(rock_num, height)

  key = (rock_num, jet_index)
  if key in cache:
    prev_step, prev_height = cache[key]
    quotient, remainder = divmod(1_000_000_000_000 - step, step - prev_step)
    if remainder == 0:
      height += (height - prev_height) * quotient
      break
  else:
    cache[key] = step, height

  while True:
    push = jet_patterns[jet_index]
    jet_index = (jet_index + 1) % len(jet_patterns)
    if push == '>':
      rock.pushRight(graph)
    else:
      rock.pushLeft(graph)
    obstructed = rock.fall(graph)
    if obstructed:
      break

  graph.update(rock.points)
  height = max(height, rock.highest())

# answer: 1560919540245
print(height)
