from typing import List

# 9. Palindrome Number

class Solution:
    def isPalindrome(self,x):
        x = str(x)
        n = len(x)
        i = 0
        j = n-1

        while i < j:
            if x[i] != x[j]:
                return False

            i += 1
            j -= 1

        return True