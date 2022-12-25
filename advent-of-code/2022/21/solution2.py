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
    monkeys[waiting_monkey_id] = WaitingMonkey(operation, left_monkey_id,
                                               right_monkey_id)

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

monkey_values = {}

def dfs(monkey_id):
  if monkey_id == "humn":
    monkey_values[monkey_id] = float('inf')
  else:
    monkey = monkeys[monkey_id]
    if type(monkey) == NumberMonkey:
      monkey_values[monkey_id] = monkey.value
    else:
      left, right = dfs(monkey.left_monkey_id), dfs(monkey.right_monkey_id)
      if left == float('inf') or right == float('inf'):
        monkey_values[monkey_id] = float('inf')
      else:
        monkey_values[monkey_id] = operations[monkey.operation](left, right)
  return monkey_values[monkey_id]

dfs("root")

def wanted_dfs(monkey_id, wanted_value):
  if monkey_id == "humn":
    return wanted_value
  else:
    monkey = monkeys[monkey_id]
    op = monkey.operation
    left, right = monkey_values[monkey.left_monkey_id], monkey_values[
        monkey.right_monkey_id]
    if left == float('inf'):
      if op == '+':
        return wanted_dfs(monkey.left_monkey_id, wanted_value - right)
      elif op == '-':
        return wanted_dfs(monkey.left_monkey_id, wanted_value + right)
      elif op == '*':
        return wanted_dfs(monkey.left_monkey_id, wanted_value // right)
      else:
        return wanted_dfs(monkey.left_monkey_id, wanted_value * right)
    else:
      if op == '+':
        return wanted_dfs(monkey.right_monkey_id, wanted_value - left)
      elif op == '-':
        return wanted_dfs(monkey.right_monkey_id, left - wanted_value)
      elif op == '*':
        return wanted_dfs(monkey.right_monkey_id, wanted_value // left)
      else:
        return wanted_dfs(monkey.right_monkey_id, left // wanted_value)

root_monkey = monkeys["root"]
root_left_value, root_right_value = monkey_values[
    root_monkey.left_monkey_id], monkey_values[root_monkey.right_monkey_id]
wanted_value = root_left_value if root_left_value != float(
    'inf') else root_right_value

# answer: 3887609741189
print(
    wanted_dfs(
        root_monkey.left_monkey_id if root_left_value == float('inf') else
        root_monkey.right_monkey_id, wanted_value))
