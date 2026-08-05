class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = defaultdict(int)
        lo = 0
        longest = 0
        for i, ch in enumerate(s):
            table[ch] += 1
            curLen = i-lo+1
            maxFreq = max(table.values())
            if curLen - maxFreq > k:
                table[s[lo]] -= 1
                lo += 1
            longest = max(longest, i - lo + 1)
        return longest
        