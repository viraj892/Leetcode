from typing import List

# [1,2,3,4,5,6,7]
# [7,1,2,3,4,5,6]
class Solution:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        move = k % length

        nums[0:length] = nums[-move:] + nums[:-move]
        return nums
        # if len(nums) == 0 or k == 0:
        #     return
        # else:
        #     for i in range(0, k):
        #         rest = nums[0:-1]
        #         nums[0] = nums[-1]
        #         nums[1:]=rest
        #     return nums


n = Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
print(n)
