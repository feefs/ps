import os
import re
import operator
from collections import deque

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

groups = f.read().split('\n\n')

class Monkey:
  def __init__(self, items, operation, test):
    self.items = items
    self.operation = operation
    self.test = test
    self.inspection_count = 0

def operation_factory(op_string, op_target_string):
  op = operator.add if op_string == '+' else operator.mul
  op_target = int(op_target_string) if op_target_string else None
  return lambda v: op(v, op_target if op_target else v)

def test_factory(test_value, true_monkey, false_monkey):
  return lambda v: true_monkey if v % test_value == 0 else false_monkey

monkeys = {}
for g in groups:
  lines = list(map(lambda l: l.strip(), g.splitlines()))

  number = int(re.findall(r"Monkey (\d*):", lines[0])[0])
  items_string = re.findall(r"Starting items: (.*)", lines[1])[0]

  op_string = re.findall(r"Operation: new = old (.).*", lines[2])[0]
  op_target_string = re.findall(r"Operation: new = old .\s(\d*)", lines[2])[0]

  test_value = int(re.findall(r"Test: divisible by (\d*)", lines[3])[0])
  true_monkey = int(re.findall(r"If true: throw to monkey (\d*)", lines[4])[0])
  false_monkey = int(
      re.findall(r"If false: throw to monkey (\d*)", lines[5])[0])

  monkeys[number] = Monkey(
      items=deque(map(lambda s: int(s), items_string.split(', '))),
      operation=operation_factory(op_string, op_target_string),
      test=test_factory(test_value, true_monkey, false_monkey))

for _ in range(20):
  for monkey in monkeys.values():
    while monkey.items:
      monkey.inspection_count += 1
      item = monkey.items.popleft()
      new_value = monkey.operation(item) // 3
      next_monkey = monkey.test(new_value)
      monkeys[next_monkey].items.append(new_value)

inspection_counts = [m.inspection_count for m in monkeys.values()]
inspection_counts.sort()
monkey_business_level = inspection_counts[-2] * inspection_counts[-1]

# answer: 110220
print(monkey_business_level)
