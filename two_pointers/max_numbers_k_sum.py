# 1679 Max Numbers of K-Sum Pairs, Mediu

import collections

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = collections.Counter()
        operations = 0
        
        for num in nums:
            complement = k - num
            # Check if the complement exists and has a remaining count
            if counts[complement] > 0:
                operations += 1
                counts[complement] -= 1  # Use up one complement
            else:
                counts[num] += 1         # Store current number for future matching
                
        return operations      