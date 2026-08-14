# 1679 Max Numbers of K-Sum Pairs, Mediu

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  # Sort the array first
        left = 0
        right = len(nums) - 1
        operations = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1   # Sum is too small, increase the smaller number
            else:
                right -= 1  # Sum is too big, decrease the larger number
                
        return operations  

# Time Complexity 0(n)