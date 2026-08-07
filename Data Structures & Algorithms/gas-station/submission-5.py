class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l, r = 0, None
        circuit = False
        while (not r or l != r):
            tank = gas[l]
            tank -= cost[l]
            # print("start",l,r,tank)
            while (tank >= 0 and (r == None or l != r)):
                if r == None:  r = l + 1
                else: r += 1
                if r == len(cost): 
                    r = 0
                    circuit = True
                tank += gas[r]
                tank -= cost[r]
                # print("inside",l,r,tank)
            if l == r: return l
            elif circuit: return -1
            elif r: 
                l = r+1
                if l == len(cost): return -1
                r = None
            else: 
                l += 1
                if l == len(cost): return -1

                

