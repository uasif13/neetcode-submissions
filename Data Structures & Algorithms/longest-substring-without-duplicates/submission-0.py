class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        longestLength = 0
        lo = 0
        for i, ch in enumerate(s):
            if ch in table:
                lo = max(lo, table[ch]+1)
            longestLength = max(longestLength, i-lo+1)
            table[ch] = i
        return longestLength