# 605 Can Place Flowers, array / string

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowers = 0
        length = len(flowerbed)
        
        for i in range(len(flowerbed)):
            if not flowerbed[i] == 1:
                if i == 0 or flowerbed[i-1] == 0:
                    if i == length - 1 or flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flowers += 1
        if flowers >= n:
            return True

        return False