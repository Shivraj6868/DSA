from typing import List

# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        ans = []

        for i in nums:
            current_sum += i
            ans.append(current_sum)
    
        return ans