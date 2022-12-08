import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

overlapping_assignments = 0
for l in f:
  value = l.strip()
  assignment_one, assignment_two = value.split(",")
  l1, r1 = assignment_one.split("-")
  l2, r2 = assignment_two.split("-")
  l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2)
  if l1 > l2:
    l1, r1, l2, r2 = l2, r2, l1, r1
  if r1 >= l2:
    overlapping_assignments += 1

# answer: 895
print(overlapping_assignments)
