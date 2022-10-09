# 2432. The Employee That Worked on the Longest Task
class Solution:
  def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
    longest = float('-inf')
    result_id = float('inf')
    prev_end = 0

    for e_id, end in logs:
      duration = end - prev_end
      if duration == longest and e_id < result_id:
        result_id = e_id
      elif duration > longest:
        result_id = e_id
        longest = duration
      prev_end = end

    return result_id
