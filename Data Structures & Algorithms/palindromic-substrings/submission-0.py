class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i, ch in enumerate(s):
            lo = i
            hi = i
            while (lo >= 0 and hi < len(s) and s[lo] == s[hi]):
                count += 1
                lo -= 1
                hi += 1
            lo = i
            hi = i+1
            while (lo >= 0 and hi < len(s) and s[lo] == s[hi]):
                count += 1
                lo -= 1
                hi += 1
        return count