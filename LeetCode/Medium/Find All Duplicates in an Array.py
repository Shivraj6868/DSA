from typing import List

# 442.Find All Duplicates in an Array 

# Brute force solution 
# - Time complexity : O(n^2).
# - Space Complexity : O(k), where k is the number of duplicate elements stored.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup_arr = []

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    if nums[i] not in dup_arr:
                        dup_arr.append(nums[i])

        return list(dup_arr)
    

# Optimised Solution 
# - Time Complexity O(n)
# - Space Complexity O(n)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        dup_arr = []

        for i in nums:
            if i in seen:
                dup_arr.append(i)
            else:
                seen.add(i)

        return dup_arr