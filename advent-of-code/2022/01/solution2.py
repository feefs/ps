import os
import heapq

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'))

top_three_elves = []
current_elf_calories = 0
for l in f:
  value = l.strip()
  if value:
    current_elf_calories += int(value)
  else:
    if len(top_three_elves) < 3:
      heapq.heappush(top_three_elves, current_elf_calories)
    elif current_elf_calories > top_three_elves[0]:
      heapq.heappop(top_three_elves)
      heapq.heappush(top_three_elves, current_elf_calories)
    current_elf_calories = 0

if len(top_three_elves) < 3:
  heapq.heappush(top_three_elves, current_elf_calories)
elif current_elf_calories > top_three_elves[0]:
  heapq.heappop(top_three_elves)
  heapq.heappush(top_three_elves, current_elf_calories)

# answer: 200945
print(sum(top_three_elves))
