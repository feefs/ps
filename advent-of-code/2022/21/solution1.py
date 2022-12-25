import os
import re
import operator

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

class NumberMonkey:
  def __init__(self, value):
    self.value = value

class WaitingMonkey:
  def __init__(self, operation, left_monkey_id, right_monkey_id):
    self.operation = operation
    self.left_monkey_id = left_monkey_id
    self.right_monkey_id = right_monkey_id

monkeys = {}
graph = {}
root_monkey = None
for l in f:
  value = l.strip()
  if match := re.search(r"([\w]{4}):\s(\d+)", value):
    monkey_id, number = match.groups()
    number = int(number)
    monkeys[monkey_id] = NumberMonkey(number)
  elif match := re.search(r"([\w]{4}):\s([\w]{4})\s(.)\s([\w]{4})", value):
    waiting_monkey_id, left_monkey_id, operation, right_monkey_id = match.groups(
    )
    op = None
    if operation == '+':
      op = operator.add
    elif operation == '-':
      op = operator.sub
    elif operation == '*':
      op = operator.mul
    elif operation == '/':
      op = operator.floordiv
    monkeys[waiting_monkey_id] = WaitingMonkey(op, left_monkey_id,
                                               right_monkey_id)

def dfs(monkey_id):
  monkey = monkeys[monkey_id]
  if type(monkey) == NumberMonkey:
    return monkey.value
  else:
    return monkey.operation(dfs(monkey.left_monkey_id),
                            dfs(monkey.right_monkey_id))

# answer: 194501589693264
print(dfs("root"))
