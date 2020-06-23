import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest_k_elements = []
        heapq.heapify(nums)
        print(heapq.nlargest(k, nums))
        while k > 0:
            max = nums[0]
            for n in nums:
                if n > max:
                    max = n
            largest_k_elements.append(max)
            nums.remove(max)
            k -= 1
        return largest_k_elements[k - 1]


# print(Solution().findKthLargest([6, 4, 5, 87, 12, 34], 3))

a = [1, 2, 3, 2]
