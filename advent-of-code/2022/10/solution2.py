import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

crt = [['.' for _ in range(40)] for _ in range(6)]

def draw(register_value, cycle):
  row = (cycle - 1) // 40
  column = (cycle - 1) % 40
  if abs(register_value - column) <= 1:
    crt[row][column] = '#'

register_value = 1
cycle = 1
draw(register_value, cycle)
for l in f:
  draw(register_value, cycle)
  value = l.strip()
  if value == "noop":
    cycle += 1
  else:
    cycle += 1
    draw(register_value, cycle)
    _, num = value.split()
    register_value += int(num)
    cycle += 1

# answer: FCJAPJRE
for row in crt:
  print("".join(row))
