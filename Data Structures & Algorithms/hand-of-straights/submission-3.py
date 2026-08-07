class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand) % groupSize != 0: return False
        groups = [[] for _ in range(len(hand)//groupSize)]
        table = Counter(hand)
        
        minimum_index = 0
        curr = hand[minimum_index]

        
        s = sum(table.values())
        i = 0
        while s > 0:
            if table[curr] == 0: return False
            groups[i].append(curr)
            table[curr] -= 1
            s -= 1
            if s == 0:
                if i == len(hand)/groupSize-1: return True
                else: return False
            if len(groups[i]) == groupSize:
                while table[hand[minimum_index]] == 0:
                    minimum_index += 1
                curr = hand[minimum_index]
                i += 1
            else:
                curr += 1
            #print(table, groups)
            
            

