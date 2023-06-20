class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


a = Solution()

print(a.containsDuplicate([1, 2, 3, 4]))  # False
print(a.containsDuplicate([1, 2, 3, 4, 1]))  # True
print(a.containsDuplicate([1, 2, 3, 4, 3]))  # False
