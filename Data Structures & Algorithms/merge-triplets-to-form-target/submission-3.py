class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = 1, 1, 1


        for i in range(len(triplets)):
            print(first, second, third)
            if (triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]) or (triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]) or (triplets[i][2] == target[2] and triplets[i][1] <= target[1] and triplets[i][0] <= target[0]):
                first = max(first, triplets[i][0])
                second = max(second, triplets[i][1])
                third = max(third, triplets[i][2]) 
            
        return first == target[0] and second == target[1] and third == target[2]