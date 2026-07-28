# 11 Container with Most Water, Two Pointers

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        largest = 0

        while left < right:
            area = (right - left) * (min(height[left], height[right]))
            if area > largest:
                largest = area
            if height[left] > height[right]:
                right -=1
            else:
                left += 1

        return largest