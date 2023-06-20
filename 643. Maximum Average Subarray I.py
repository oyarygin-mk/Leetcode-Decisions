from collections import deque


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        q = deque([])

        ans = -float('inf')

        cnt = 0
        cur = 0

        for i in range(0, len(nums)):
            cur += nums[i]
            cnt += 1

            if cnt == k:
                ans = max(ans, cur / k)

            if cnt > k:
                cur -= nums[i - k]
                ans = max(ans, cur / k)
        return ans


a = Solution()

print(a.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
