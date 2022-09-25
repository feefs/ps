# 2420. Find All Good Indices
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # ni[i] = longest non-increasing run that runs from start to i inclusive
        # nd[i] = longest non-decreasing run that runs from i to end inclusive
        ni, nd = [1] * n, [1] * n
        for i in range(1, n):
            # right number (current) is non-increasing if it is <= the left number (previous)
            if nums[i] <= nums[i - 1]:
                ni[i] = 1 + ni[i - 1]

        for i in reversed(range(n - 1)):
            # right number (next) is non-decreasing if it is >= the left number (current)
            if nums[i + 1] >= nums[i]:
                nd[i] = 1 + nd[i + 1]

        result = []
        for i in range(n - (2 * k)):
            index = i + k
            # off by one since we want run lengths that end before and after index
            if ni[index - 1] >= k and nd[index + 1] >= k:
                result.append(i + k)

        return result
