from typing import List


#  1941. Check if All Characters Have Equal Number of Occurrences


# Time complexity : O(n)
# Space Complexity : O(k)

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        freq = {}

        for i in s:
            freq[i] = freq.get(i,0) + 1

        return len(set(freq.values())) == 1 