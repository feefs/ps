# 2788. Split Strings by Separator
class Solution:
  def splitWordsBySeparator(self, words: List[str],
                            separator: str) -> List[str]:
    result = []
    for w in words:
      result.extend(filter(lambda splitted: splitted != "", w.split(separator)))

    return result
