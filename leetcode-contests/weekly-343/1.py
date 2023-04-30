# 2660. Determine the Winner of a Bowling Game
class Solution:
  def isWinner(self, player1: List[int], player2: List[int]) -> int:
    def score(pins):
      result = 0
      for i, p in enumerate(pins):
        strike = False
        if i > 0 and pins[i - 1] == 10:
          strike = True
        if i > 1 and pins[i - 2] == 10:
          strike = True
        if strike:
          result += 2 * p
        else:
          result += p
      return result

    player1_score, player2_score = score(player1), score(player2)

    if player1_score == player2_score:
      return 0
    else:
      return 1 if player1_score > player2_score else 2
