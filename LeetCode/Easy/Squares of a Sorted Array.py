from typing import List

# 977. Squares of a Sorted Array
 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_arr = []
        
        for i in nums:
            square_arr.append(i**2)

        square_arr.sort()

        return square_arr