import os

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'))

elf_with_most_calories = 0
current_elf_calories = 0
for line in f:
  value = line.strip()
  if value:
    current_elf_calories += int(value)
  else:
    elf_with_most_calories = max(elf_with_most_calories, current_elf_calories)
    current_elf_calories = 0

elf_with_most_calories = max(elf_with_most_calories, current_elf_calories)

# answer: 69693
print(elf_with_most_calories)
