class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]*(len(s)+2)
        i = len(s)-1
        zeroFlag = False
        while i >= 0:
            if i > 0 and s[i] == "0" and (s[i-1] == "1" or s[i-1] == "2"):
                dp[i] = dp[i+1]
                dp[i-1] = dp[i]
                i -= 2
                zeroFlag = True
            elif s[i] == "0":
                return 0
            elif zeroFlag:
                dp[i] = dp[i+1]
                i -= 1
                zeroFlag = False
            elif i < len(s) - 1 and s[i] == "1":
                dp[i] = dp[i+1] + dp[i+2]
                i -= 1
            elif i < len(s) - 1 and s[i] == "2":
                if i == len(s) - 1 or s[i+1] == "7" or s[i+1] == "8" or s[i+1] == "9":
                    dp[i] = dp[i+1]
                    i -= 1
                else:
                    dp[i] = dp[i+1] + dp[i+2]
                    i -= 1
            else:
                dp[i] = dp[i+1]
                i -= 1
        
        print(dp)
        return dp[0]
            