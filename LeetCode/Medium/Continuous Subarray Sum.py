from typing import List

# 523. Continuous Subarray Sum 

# Given an integer array arr and an integer k, return true if nums has a good subarray or false otherwise.

# - A good subarray is a subarray where:
# - its length is at least two, and
# - the sum of the elements of the subarray is a multiple of k.

# Note that:
# - A subarray is a contiguous part of the array.
# - An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# Brute Force solution :
# - Time complexity : O(n^2)
# - Space Complexity : O(1)

arr = [23, 2, 6, 4, 7]
n = len(arr)
k = 6

value = False
for i in range(n):
    current_sum = arr[i]
    for j in range(i+1, n):
        current_sum += arr[j]
        
        if current_sum % k == 0:
            value = True
            break
            
        if value:
            break
if value:
    print("True")
else:
    print("False")
