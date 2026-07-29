# 1207 Unique Number of Occurances, Hashmap

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        
        occurances = {}
        unique = set()
        
        for num in arr:
            if num in occurances:
                occurances[num] += 1
            else:
                occurances[num] = 1
        
        for key, value in occurances.items():
            unique.add(value)
        
        if len(unique) < len(occurances):
            return False
        
        return True
        
# Time Complexity O(2n)