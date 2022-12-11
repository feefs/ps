import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

register_value = 1
cycle = 1
total_signal_strength = 0
for l in f:
  if cycle % 40 == 20:
    total_signal_strength += cycle * register_value
  value = l.strip()
  if value == "noop":
    cycle += 1
  else:
    if (cycle + 1) % 40 == 20:
      total_signal_strength += (cycle + 1) * register_value
    _, num = value.split()
    register_value += int(num)
    cycle += 2

# answer: 12880
print(total_signal_strength)
