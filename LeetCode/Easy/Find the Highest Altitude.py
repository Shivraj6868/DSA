from typing import List

# 1732. Find the Highest Altitude

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        pre_sum = [0,]

        for i in gain:
            total += i
            pre_sum.append(total)

        return max(pre_sum)
    


