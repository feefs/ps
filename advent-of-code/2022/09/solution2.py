import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

diff = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def compute_knot(moved_pos, following_pos):
  mx, my = moved_pos
  fx, fy = following_pos
  dx, dy = abs(mx - fx), abs(my - fy)
  if (dx == 2 and dy == 0) or (dx == 0 and dy == 2):
    return ((mx + fx) // 2, (my + fy) // 2)
  manhattan_distance = dx + dy
  if manhattan_distance <= 2:
    return following_pos
  else:
    return diagonal_move(moved_pos, following_pos)

def diagonal_move(moved_pos, following_pos):
  mx, my = moved_pos
  fx, fy = following_pos
  dx, dy = 1 if mx - fx > 0 else -1, 1 if my - fy > 0 else -1
  return (fx + dx, fy + dy)

knots = [(0, 0) for _ in range(10)]
visited_positions = {(0, 0)}
for l in f:
  direction, steps = l.strip().split()
  steps = int(steps)
  for _ in range(steps):
    hx, hy = knots[0]
    dx, dy = diff[direction]
    knots[0] = (hx + dx, hy + dy)
    for i in range(9):
      knots[i + 1] = compute_knot(knots[i], knots[i + 1])
    visited_positions.add(knots[-1])

# answer: 2545
print(len(visited_positions))
