# 2589. Minimum Time to Complete All Tasks
class Solution:
  def findMinimumTime(self, tasks: List[List[int]]) -> int:
    """
    sort intervals by end to maximize overlap
    for the current interval
      parallelize with as many previous on_timestamps as possible
        subtract from duration
      schedule remaining duration
        already parallelized as much as possible with previous step
        => fill in as many unused "slots" as possible greedily from the right
    """
    tasks.sort(key=lambda task: task[1])
    on_timestamps = set()
    for task in tasks:
      start, end, duration = task
      # parallelize with as many previous on_timestamps as possible
      for slot in range(start, end + 1):
        if slot in on_timestamps:
          duration -= 1
      # schedule remaining duration of the current task
      slot = end
      while duration > 0:
        if slot not in on_timestamps:
          on_timestamps.add(slot)
          duration -= 1
        slot -= 1

    return len(on_timestamps)
