class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if (num == 1):
            return True

        left = 1
        right = num // 2

        while (left <= right):

            mid = (left + right) // 2
            sq = mid * mid

            if (sq == num):
                return True
            if (sq < num):
                left = mid + 1
            else:
                right = mid - 1

        return False


a = Solution()

print(a.isPerfectSquare(9))
