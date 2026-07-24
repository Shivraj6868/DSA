from typing import List

# 349.Intersection of Two Arrays
# - Time Complexity : O(n + m)
# - Space Complexity : O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        answer = []

        for num in nums2:
            if num in seen:
                answer.append(num)
                seen.remove(num)      

        return answer