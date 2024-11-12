from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for i in range(len(nums)) :
            if nums[i] == 0 :
                del nums[i]
                i = i - 1
                nums.append(0)


nums = [0, 0, 1]
solution  = Solution()

solution.moveZeroes(nums)

print(nums)