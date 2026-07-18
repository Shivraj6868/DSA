# Finding the Maximum Sum of a Contiguous Subarray

# Brute Force solution :
# - Time complexity : O(n^2)
# - Space Complexity : O(1)

arr = list(map(int, input().split()))
n = len(arr)

max_sum = arr[0]

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += arr[j]
        
        if current_sum > max_sum:
            max_sum = current_sum
            
print(max_sum)


# Optimized Solution using Kadane's Algorithm : 
# - Time complexity = O(n)
# - Space complexity = O(1)

arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = 0

for i in arr:
    current_sum += i
    max_sum = max(max_sum, current_sum)
    
    if current_sum < 0:
        current_sum = 0
        
print(max_sum)