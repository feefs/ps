# 2491. Divide Players Into Teams of Equal Skill
class Solution:
  def dividePlayers(self, skill: List[int]) -> int:
    total = sum(skill)
    num_teams = len(skill) // 2
    target = total // num_teams

    skill.sort()
    l, r = 0, len(skill) - 1
    pairs = []
    while l < r:
      if skill[l] + skill[r] != target:
        return -1
      pairs.append(skill[l] * skill[r])
      l += 1
      r -= 1

    return sum(pairs)
