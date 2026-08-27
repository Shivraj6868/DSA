from typing import List

# 169. Majority Element

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1

        for num, count in freq.items():
            if count > n//2:
                return num

