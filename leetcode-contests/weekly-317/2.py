# 2456. Most Popular Video Creator
class Solution:
  def mostPopularCreator(self, creators: List[str], ids: List[str],
                         views: List[int]) -> List[List[str]]:
    counts = {}
    most_popular_video = {}
    for c, i, v in zip(creators, ids, views):
      counts[c] = counts.get(c, 0) + v
      vid = most_popular_video.get(c, (0, "zzzzz"))
      if v > vid[0] or (v == vid[0] and i < vid[1]):
        most_popular_video[c] = (v, i)

    items = list(counts.items())
    items.sort(key=lambda i: i[1], reverse=True)
    highest_popularity = items[0][1]
    result = []
    for c, v in items:
      if v == highest_popularity:
        result.append([c, most_popular_video[c][1]])

    return result
