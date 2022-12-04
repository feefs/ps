# 2490. Circular Sentence
class Solution:
  def isCircularSentence(self, sentence: str) -> bool:
    words = sentence.split()
    for i in range(len(words) - 1):
      w1, w2 = words[i], words[i + 1]
      if w1[-1] != w2[0]:
        return False
      i += 1

    return words[-1][-1] == words[0][0]
