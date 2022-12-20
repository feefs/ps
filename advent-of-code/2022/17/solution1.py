import os
import itertools

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

jet_patterns = itertools.cycle(f.read().strip())
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
graph = set()
for _ in range(2022):
  rock_num = next(rock_numbers)
  rock = Rock(rock_num, height)

  while True:
    push = next(jet_patterns)
    if push == '>':
      rock.pushRight(graph)
    else:
      rock.pushLeft(graph)
    obstructed = rock.fall(graph)
    if obstructed:
      break

  graph.update(rock.points)
  height = max(height, rock.highest())

# answer: 3151
print(height)
