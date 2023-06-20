class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        par = []
        for i in range(0, len(nums)):
            par.append((i, nums[i]))

        par.sort(key=lambda x: x[1])

        i = 0
        j = len(par) - 1

        while par[i][1] + par[j][1] != target:
            if (par[i][1] + par[j][1] < target):
                i += 1
            else:
                j -= 1
        return [par[i][0], par[j][0]]
