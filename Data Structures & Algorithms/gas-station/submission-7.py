class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        result = 0
        i = 0
        circuit = 2
        loop = 2
        while (loop > 0):
            total += gas[i] - cost[i]
            if total < 0: 
                total = 0
                result = i + 1
                circuit = 2
            if result >= len(gas): return -1
            i += 1
            if i == len(gas):
                i = 0
                circuit -= 1
                loop -= 1
            if circuit == 0: return result
            if loop == 0: return -1
            
            #print(i, result, total)
                        

