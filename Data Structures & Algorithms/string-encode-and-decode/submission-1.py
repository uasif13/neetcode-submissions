class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\n\n\n".join(strs) + "\n\n\n"+str(len(strs))

    def decode(self, s: str) -> List[str]:
        s = s.split("\n\n\n")
        if s[-1] == "0": return []
        else: return s[:-1]