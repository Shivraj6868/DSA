# Find Second Largest Element in Array

class Solution:
    def getSecondLargest(self, arr):
        # code here
        large = max(arr)
        second_largest = float('-inf')
        
        for i in arr:
            if i > second_largest and i < large:
                second_largest = i
               
        if second_largest == float('-inf'):
            return -1
            
        return second_largest