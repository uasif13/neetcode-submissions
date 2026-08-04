class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict()
        for s in strs:
            sortedWord = "".join(sorted(list(s)))
            if sortedWord in table: table[sortedWord].append(s)
            else: table[sortedWord] = [s]
        return list(table.values())
        