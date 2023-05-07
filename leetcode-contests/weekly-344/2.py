# 2671. Frequency Tracker
class FrequencyTracker:
  def __init__(self):
    self.counts = defaultdict(int)
    self.freqs = defaultdict(int)

  def add(self, number: int) -> None:
    self.freqs[self.counts[number]] -= 1
    self.counts[number] += 1
    self.freqs[self.counts[number]] += 1

  def deleteOne(self, number: int) -> None:
    if self.counts[number] != 0:
      self.freqs[self.counts[number]] -= 1
      self.counts[number] -= 1
      self.freqs[self.counts[number]] += 1

  def hasFrequency(self, frequency: int) -> bool:
    return self.freqs[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
