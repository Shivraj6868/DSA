# Counting How many elements in the array are strictly greater than its initial minimum value.

arr = list(map(int, input().split()))
n = len(arr)

min_value = arr[0]

# finding minimum element in array 
for i in range(1, n):
    if min_value > arr[i]:
        min_value = arr[i]

count = 0

# Counting Greater element than initial minimum element in array
for j in range(n):
    if min_value < arr[j]:
        count += 1


print(count)



