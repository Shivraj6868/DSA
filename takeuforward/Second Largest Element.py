# find Second Largest Element in array

class Solution:
    def secondLargestElement(self, nums):
        largest = max(nums)
        second_largest = float('-inf')

        for i in nums:
            if i > second_largest and i < largest:
                second_largest = i

        if second_largest == float('-inf'):
            return -1

        return second_largest
    
    print(secondLargestElement)