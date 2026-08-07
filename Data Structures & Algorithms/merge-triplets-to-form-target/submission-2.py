class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort(key = lambda triplet: (triplet[0],triplet[1],triplet[2]))
        j = 0
        first = triplets[0][0]
        second = triplets[0][1]
        third = triplets[0][2]
        
        while (j < len(triplets) and (first > target[0] or second > target[1] or third > target[2] )):
            first = triplets[j][0]
            second = triplets[j][1]
            third = triplets[j][2]
            j+=1


        for i in range(j+1,len(triplets)):
            print(first, second, third)
            if first > target[0] or second > target[1] or third > target[2]: return False
            if (triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]) or (triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]) or (triplets[i][2] == target[2] and triplets[i][1] <= target[1] and triplets[i][0] <= target[0]):
                first = max(first, triplets[i][0])
                second = max(second, triplets[i][1])
                third = max(third, triplets[i][2]) 
            
        return first == target[0] and second == target[1] and third == target[2]