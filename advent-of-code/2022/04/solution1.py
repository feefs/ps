import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

fully_contained_assignments = 0
for l in f:
  value = l.strip()
  assignment_one, assignment_two = value.split(",")
  l1, r1 = assignment_one.split("-")
  l2, r2 = assignment_two.split("-")
  l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2)
  if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
    fully_contained_assignments += 1

# answer: 580
print(fully_contained_assignments)
