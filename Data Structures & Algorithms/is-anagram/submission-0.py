class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = {}
        for i in s:
            if i not in s_dict: s_dict[i] = 1
            else: s_dict[i] +=1
        t_dict = {}
        for j in t:
            if j not in t_dict: t_dict[j] = 1
            else: t_dict[j] +=1
        return s_dict == t_dict
