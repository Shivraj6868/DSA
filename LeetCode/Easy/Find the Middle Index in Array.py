from typing import List

# 1991. Find the Middle Index in Array

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        n = len(nums)
        total = 0
        pre_sum = []

        for i in nums:
            total += i
            pre_sum.append(total)

        for i in range(n):

            left_sum = pre_sum[i]-nums[i]
            right_sum = total - pre_sum[i]

            if left_sum == right_sum:
                return i

        return -1
        