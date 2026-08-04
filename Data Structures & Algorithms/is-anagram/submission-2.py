class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        table = {}
        for ch in s:
            if ch in table: table[ch] += 1
            else: table[ch] = 1
        for ch in t:
            if ch not in table or table[ch] == 0: return False
            table[ch] -= 1
        return sum(table.values()) == 0