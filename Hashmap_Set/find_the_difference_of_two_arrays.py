# 2215 Find the Difference of Two Arrays

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer1_dict = {} 
        answer2_dict = {}
        answer1= []
        answer2 = []
        
        for i in range(len(nums1)):
            answer1_dict[nums1[i]] = i
        remaining1_dict= answer1_dict.copy()
        for i in range(len(nums2)):
            if nums2[i] not in answer1_dict:
                answer2_dict[nums2[i]] = i
            else:
                remaining1_dict.pop(nums2[i], None)
        for key in remaining1_dict:
            answer1.append(key)
        for key in answer2_dict:
            answer2.append(key)
        return [answer1, answer2]
        
# O(n+m) Time Complexity
