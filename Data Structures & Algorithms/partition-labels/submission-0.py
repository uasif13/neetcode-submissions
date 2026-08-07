class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = {}
        for i, ch in enumerate(s):
            if ch in table: table[ch].append(i)
            else: table[ch] = [i]
        result = []
        l,r = 0,0
        while (l < len(s)):
            curr = l
            while curr <= r:
                r = max(r, table[s[curr]][-1])
                curr += 1
            result.append(r-l+1)
            l = curr
            r = curr
        return result
            