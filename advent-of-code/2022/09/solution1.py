import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

diff = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def compute_tail(head_pos, tail_pos):
  hx, hy = head_pos
  tx, ty = tail_pos
  dx, dy = abs(hx - tx), abs(hy - ty)
  if (dx == 2 and dy == 0) or (dx == 0 and dy == 2):
    return ((hx + tx) // 2, (hy + ty) // 2)
  manhattan_distance = dx + dy
  if manhattan_distance <= 2:
    return tail_pos
  else:
    return diagonal_move(head_pos, tail_pos)

def diagonal_move(head_pos, tail_pos):
  hx, hy = head_pos
  tx, ty = tail_pos
  dx, dy = 1 if hx - tx > 0 else -1, 1 if hy - ty > 0 else -1
  return (tx + dx, ty + dy)

head_pos = (0, 0)
tail_pos = (0, 0)
visited_positions = {(0, 0)}
for l in f:
  direction, steps = l.strip().split()
  steps = int(steps)
  for _ in range(steps):
    hx, hy = head_pos
    dx, dy = diff[direction]
    head_pos = (hx + dx, hy + dy)
    tail_pos = compute_tail(head_pos, tail_pos)
    visited_positions.add(tail_pos)

# answer: 6030
print(len(visited_positions))
