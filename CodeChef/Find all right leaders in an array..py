# Print elements(Leaders) having no greater element on their right side.

arr = list(map(int, input().split()))
n = len(arr)

leader = [arr[n-1]]
max_val = arr[n-1]

for i in range(n-2,-1,-1):
    if arr[i] > max_val:
        max_val = arr[i]
        leader.append(arr[i])
        
leader.reverse()
print(*leader)