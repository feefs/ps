import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

class Node():
  def __init__(self, val, prv=None, nxt=None):
    self.val = val
    self.prv = prv
    self.nxt = nxt

class Sentinel():
  def __init__(self):
    self.head = self.tail = None

  # node's prv and nxt must be None
  def push_front(self, node):
    if self.head == None:
      self.head = self.tail = node
    else:
      self.head.prv, node.nxt = node, self.head
      self.head = self.head.prv

  # node's prv and nxt must be None
  def push_end(self, node):
    if self.head == None:
      self.head = self.tail = node
    else:
      self.tail.nxt, node.prv = node, self.tail
      self.tail = self.tail.nxt

  # returns head with prv + nxt set to None and updates self.head
  def pop_head(self):
    tmp = self.head
    self.head = self.head.nxt
    if self.head:
      self.head.prv = None
    tmp.prv = tmp.nxt = None
    return tmp

  # returns tail with prv + nxt set to None and updates self.tail
  def pop_tail(self):
    tmp = self.tail
    self.tail = self.tail.prv
    if self.tail:
      self.tail.nxt = None
    tmp.prv = tmp.nxt = None
    return tmp

  def swap(self, left, right):
    # point left - 1 and right + 1 correctly
    left.prv.nxt, right.nxt.prv = right, left
    # point left and right correctly
    left.prv, left.nxt, right.prv, right.nxt = right, right.nxt, left.prv, left

  # shifts the node to the left
  def shift_backwards(self, node):
    for _ in range(abs(node.val)):
      if node == self.head:
        same_tail = self.pop_tail()
        self.push_end(self.pop_head())
        self.push_end(same_tail)
      elif node.prv == self.head:
        same_head = self.pop_head()
        tmp = self.pop_head()
        self.push_end(tmp)
        self.push_front(same_head)
      elif node == self.tail:
        tmp1 = self.pop_tail()
        tmp2 = self.pop_tail()
        self.push_end(tmp1)
        self.push_end(tmp2)
      else:
        self.swap(node.prv, node)

  # shifts the node to the right
  def shift_forwards(self, node):
    for _ in range(node.val):
      if node == self.tail:
        same_head = self.pop_head()
        self.push_front(self.pop_tail())
        self.push_front(same_head)
      elif node.nxt == self.tail:
        same_tail = self.pop_tail()
        tmp = self.pop_tail()
        self.push_front(tmp)
        self.push_end(same_tail)
      elif node == self.head:
        tmp1 = self.pop_head()
        tmp2 = self.pop_head()
        self.push_front(tmp1)
        self.push_front(tmp2)
      else:
        self.swap(node, node.nxt)

sentinel = Sentinel()

zero_node = None
nodes = []
for l in f:
  value = int(l.strip())
  node = Node(value)
  nodes.append(node)
  sentinel.push_end(node)
  if node.val == 0:
    zero_node = node

for i, node in enumerate(nodes):
  if node.val > 0:
    sentinel.shift_forwards(node)
  else:
    sentinel.shift_backwards(node)

grove_coordinates = []
curr = zero_node
for i in range(1, 3001):
  curr = curr.nxt if curr != sentinel.tail else sentinel.head
  if i % 1000 == 0:
    grove_coordinates.append(curr.val)

# answer: 3466
print(sum(grove_coordinates))
