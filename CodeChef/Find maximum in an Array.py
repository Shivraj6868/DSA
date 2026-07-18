# Find maximum Number in an Array.

# Solution contain Time Complexity O(n^2) 
n = int(input())
arr = list(map(int, input().split()))

max_num = arr[0]

for i in range(n):
    for j in range(n):

        if arr[i] > arr[j]:
            max_num = arr[i]
            j+1

        if arr[i] < arr[j]:
            max_num = arr[j]
            i = j
            j+1

print(max_num)


# optimized solution, Time complexity O(n)

n = int(input())
arr = list(map(int, input().split()))

max_num = arr[0]

for i in range(n):
    if arr[i] > max_num:
        max_num = arr[i]

print(max_num)

