# 1732 Highest Altitude Sum, prefix sum

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        highest = 0
        for height in gain:
            altitude += height
            if altitude > highest:
                highest = altitude
        
        return highest
        
# Time Complexity O(n)