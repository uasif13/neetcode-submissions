class Solution:
    def checkWindow(self, tableS: dict, tableT: dict) -> bool:
        #print(tableS, tableT)
        for ch in tableT:
            if tableS[ch] < tableT[ch]: return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        tableT = defaultdict(int)
        tableS = defaultdict(int)
        smallest = 1001
        result = ""
        for ch in t:
            tableT[ch] += 1
        lo = 0
        for i, ch in enumerate(s):
            tableS[ch] += 1
            #print("for",i,lo, result)
            while (self.checkWindow(tableS, tableT)):
                curLen = i - lo + 1
                if curLen < smallest:
                    smallest = curLen
                    result = s[lo:i+1]
                tableS[s[lo]] -= 1
                lo += 1
                #print("while",i,lo, result)
        return result
        