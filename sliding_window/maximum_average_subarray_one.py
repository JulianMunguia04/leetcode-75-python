# Leetcode 643 Sliding Window

class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        total = 0
        largest = float("-inf")

        for right in range(len(nums)):
            total += nums[right]

            if right + 1 >= k:
                if total > largest:
                    largest = total

                total -= nums[left]
                left += 1

        return largest / float(k)

        
# Time Complexity