# 334 Increasing Triplet Subsequence, Array / String

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first = float('inf')
        second = float('inf')

        for num in nums:
          if num <= first:
            first = num
          elif num <= second:
            second = num
          else:
            return True
        
        return False

# Time Complexity O(n) with n being the amount of integers in nums