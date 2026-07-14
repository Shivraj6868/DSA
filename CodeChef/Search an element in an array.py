# Search an element in an array and return YES if Element exist in Array, otherwise return NO.
def find_num(n, num, arr):

    for i in range(n):
        if arr[i] == num:
            return "YES"
        
    return "NO"


n = int(input())
num = int(input())
arr = list(map(int, input().split()))

# Calling Function.
print(find_num(n, num, arr))