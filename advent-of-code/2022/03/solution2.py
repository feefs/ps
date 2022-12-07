import os
import string
import itertools
import functools

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def get_priority(item):
  if item in string.ascii_lowercase:
    return ord(item) - ord('a') + 1
  else:
    return ord(item) - ord('A') + 27

def yield_values():
  values = iter(f.read().split())
  while chunk := list(itertools.islice(values, 3)):
    yield chunk

total_priority = 0
for group in yield_values():
  bag_sets = map(lambda bag: set(bag), group)
  group_badge = list(functools.reduce(lambda a, b: a.intersection(b),
                                      bag_sets))[0]
  total_priority += get_priority(group_badge)

# answer: 2703
print(total_priority)
