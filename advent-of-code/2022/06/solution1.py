import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

value = f.read().strip()

window = {}
for i in range(4):
  c = value[i]
  if c not in window:
    window[c] = 0
  window[c] += 1

i = 4
while i < len(value):
  if len(window) == 4:
    break
  c_to_add = value[i]
  c_to_remove = value[i - 4]
  if c_to_add not in window:
    window[c_to_add] = 0
  window[c_to_add] += 1
  window[c_to_remove] -= 1
  if window[c_to_remove] == 0:
    del window[c_to_remove]
  i += 1

# answer: 1757
print(i)
