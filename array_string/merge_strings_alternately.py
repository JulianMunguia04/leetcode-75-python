# 1768, Merge Strings Alternately, Easy

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        s = ""

        i = 0
        
        while i < len(word1):
            s += (word1[i])
            if i < len(word2):
                s += word2[i]
            i += 1
        
        if len(word2) > len(word1):
            s += word2[i::]
        
        return s
    
# Time Complexity O(n)