import os
from collections import defaultdict
import re

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

class Directory():
  def __init__(self):
    self.directories = defaultdict(lambda: Directory())
    self.files = defaultdict(lambda: 0)
    self.size = 0
    self.parent = None

root = Directory()
cwd = root

values = f.read().splitlines()
i = 0
while i < len(values):
  if match := re.search(r"\$ cd (.*)", values[i]):
    name = match.group(1)
    if name == "/":
      cwd = root
    elif name == "..":
      cwd = cwd.parent
    else:
      cwd.directories[name].parent = cwd
      cwd = cwd.directories[name]
    i += 1
  elif match := re.search(r"\$ ls", values[i]):
    i += 1
    while i < len(values):
      if re.search(r"\$.*", values[i]):
        break
      match = re.search(r"([^\s]*) ([^\s]*)", values[i])
      l, r = match.groups()
      if l == "dir":
        cwd.directories[r].parent = cwd
      else:
        file_size, file_name = int(l), r
        cwd.files[file_name] = file_size
      i += 1

def update_size_dfs(dir):
  dir.size += sum([file_size for file_size in dir.files.values()])
  size_of_children = 0
  for next_dir in dir.directories.values():
    size_of_children += update_size_dfs(next_dir)
  dir.size += size_of_children
  return dir.size

update_size_dfs(root)

def count_sizes_dfs(dir):
  total_sizes = 0
  if dir.size <= 100_000:
    total_sizes += dir.size
  for next_dir in dir.directories.values():
    total_sizes += count_sizes_dfs(next_dir)
  return total_sizes

# answer: 1334506
print(count_sizes_dfs(root))
