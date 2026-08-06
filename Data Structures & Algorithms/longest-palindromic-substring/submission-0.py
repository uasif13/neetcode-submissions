class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 1
        result = s[0]
        for i, ch in enumerate(s):
            lo = i
            hi = i
            while (lo >= 0 and hi < len(s) and s[lo] == s[hi]):
                if hi - lo + 1 > resLen:
                    resLen = hi - lo + 1
                    result = s[lo:hi+1]
                lo -= 1
                hi += 1
            
            lo = i
            hi = i+1
            while (lo >= 0 and hi < len(s) and s[lo] == s[hi]):
                if hi - lo + 1 > resLen:
                    resLen = hi - lo + 1
                    result = s[lo:hi+1]
                lo -= 1
                hi += 1
        return result
