from typing import List

# 242. Valid Anagram

# Anagram means Both stings Frequency map should be equal.

# Time Complexity : O(n)
# Space Complexity : O(k) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for i in s:
            s_freq[i] = s_freq.get(i,0) + 1

        for i in t:
            t_freq[i] = t_freq.get(i,0) + 1
        
        if s_freq == t_freq:
            return True 

        return False