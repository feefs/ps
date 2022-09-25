# 2418. Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key=lambda p: p[1], reverse=True)
        return list(map(lambda p: p[0], people))
