# 2446. Determine if Two Events Have Conflict
class Solution:
  def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
    def date_to_minutes(s):
      h, m = s.split(":")
      return (int(h) * 60) + int(m)

    s1, e1 = date_to_minutes(event1[0]), date_to_minutes(event1[1])
    s2, e2 = date_to_minutes(event2[0]), date_to_minutes(event2[1])

    if s1 > s2:
      s1, s2 = s2, s1
      e1, e2 = e2, e1

    return e1 >= s2
