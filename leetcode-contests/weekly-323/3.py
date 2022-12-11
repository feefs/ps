# 2502. Design Memory Allocator
class Allocator:
  def __init__(self, n: int):
    self.data = [0 for _ in range(n)]
    self.limit = n

  def allocate(self, size: int, mID: int) -> int:
    run_size = 0
    i = 0
    while i < self.limit:
      if self.data[i] == 0:
        run_size += 1
        i += 1
        if run_size == size:
          for j in range(i - run_size, i):
            self.data[j] = mID
          return i - run_size
      else:
        run_size = 0
        i += 1
    return -1

  def free(self, mID: int) -> int:
    result = 0
    for i, n in enumerate(self.data):
      if n == mID:
        self.data[i] = 0
        result += 1
    return result

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
