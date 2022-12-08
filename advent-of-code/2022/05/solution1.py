import os
import re

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

stacks = [['R', 'N', 'P', 'G'], ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
          ['T', 'D', 'B', 'M', 'N', 'L'], ['R', 'V', 'P', 'S', 'B'],
          ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
          ['W', 'Q', 'S', 'C', 'D', 'B', 'J'], ['F', 'Q', 'L'],
          ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
          ['L', 'P', 'B', 'V', 'M', 'J', 'F']]

for l in f:
  value = re.search(r"move (\d+) from (\d) to (\d)", l.strip())
  num_crates, source_stack, dest_stack = value.groups()
  num_crates = int(num_crates)
  source_stack = int(source_stack)
  dest_stack = int(dest_stack)
  for _ in range(num_crates):
    stacks[dest_stack - 1].append(stacks[source_stack - 1].pop())

# answer: HBTMTBSDC
print("".join(map(lambda s: s[-1], stacks)))
