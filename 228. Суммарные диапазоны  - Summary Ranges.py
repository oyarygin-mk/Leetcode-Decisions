# Асимптотическая сложность O(N) - временная сложность,  Пространственная сложность - O(1)
class Solution:
    def SummaryRanges(self):
        ranges = []
        i = 0
        while i < len(nums):
            start = nums[i]  # Начало текущего диапазона
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if (start != nums[i]):
                ranges.append(f"{start} -> {nums[i]}")
            else:
                ranges.append(f"{nums[i]}")
            i += 1
        return ranges


nums = [0, 1, 2, 4, 5, 7]
print(Solution.SummaryRanges(nums))
nums = [0, 2, 3, 4, 6, 8, 9]
print(Solution.SummaryRanges(nums))
