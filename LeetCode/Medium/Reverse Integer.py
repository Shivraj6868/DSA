from typing import List

# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31-1

        if x < 0:
            sign = -1
        else:
            sign = 1

        arr = list(str(abs(x)))
        n = len(arr)
        i = 0
        j = n-1

        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        
        reverse = int("".join(arr))
        reverse *= sign

        if reverse < int_min or reverse > int_max:
            return 0

        return reverse