import os
import string

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def get_priority(item):
  if item in string.ascii_lowercase:
    return ord(item) - ord('a') + 1
  else:
    return ord(item) - ord('A') + 27

total_priority = 0
for l in f:
  value = l.strip()
  compartment_one = value[:len(value) // 2]
  compartment_two = value[len(value) // 2:]
  compartment_one_items = set(compartment_one)
  compartment_two_items = set(compartment_two)
  shared_item = list(
      compartment_one_items.intersection(compartment_two_items))[0]
  total_priority += get_priority(shared_item)

# answer: 7795
print(total_priority)
