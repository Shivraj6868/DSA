# Sum of Array Elements
n = int(input())
arr = list(map(int, input().split()))
sum = 0

for i in arr:
    sum += i
    i+1
    
print(sum)