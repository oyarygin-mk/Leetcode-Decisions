class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        result = []
        i = 0
        n = 0
        while i < len(nums):
            if nums[i] == 0:
                n += 1
            else:
                result.append(nums[i])
            i += 1
        while n != 0:
            result.append(0)
            n -= 1
        return result


Solution.moveZeroes([1, 2, 3, 4])


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]

                j += 1


Solution.moveZeroes([1, 2, 3, 4])
