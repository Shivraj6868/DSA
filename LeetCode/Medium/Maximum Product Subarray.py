from typing import List

# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]

        current_prod = 1
        for i in nums:
            if current_prod == 0:
                current_prod = 1

            current_prod *= i
            max_prod = max(max_prod, current_prod)

        current_prod = 1
        for i in reversed(nums):
            if current_prod == 0:
                current_prod = 1

            current_prod *= i
            max_prod = max(max_prod, current_prod)

        return max_prod
    