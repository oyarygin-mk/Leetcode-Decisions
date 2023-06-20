class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]

        for i in range(1, n + 1):

            cur = 0

            while i:
                cur += i & 1
                i >>= 1
            ans.append(cur)

        return ans

