# 1431 Kids with the greatest number of candies. Array / String

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        most = 0
        most_candies = []
        
        for i in range(len(candies)):
            if candies[i] > most:
                most = candies[i]
                
        for kid in candies:
            if kid + extraCandies >= most:
                most_candies.append(True)
            else:
                most_candies.append(False)
                
        return most_candies
            
        
# Time Complexity O(n)