class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        new = 0
        orig = x

        while x:
            x, y = divmod(x, 10)

            new = new * 10 + y

        return new == orig


a = Solution()
print(a.isPalindrome(1212221))  # False
print(a.isPalindrome(1212))  # False
print(a.isPalindrome(121))  # True
