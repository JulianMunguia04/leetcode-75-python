#Notes Strings are dynamic arrays of characters

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        rtype = ""
        
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                rtype += word1[i]
            if i < len(word2):
                rtype += word2[i]
        return rtype

#Time Complexity O(n), n being the count of numbers in nums. ie Linear Time