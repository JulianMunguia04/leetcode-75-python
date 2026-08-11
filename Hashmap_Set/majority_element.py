# 169 Majority Element, Hashmap, Easy

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        hashmap = {}
        highest = 0
        largest = 0

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else: 
                hashmap[nums[i]] += 1
            if hashmap[nums[i]] > highest:
                highest = hashmap[nums[i]]
                largest = nums[i]

        return largest

# Time Complexity O(n)