# 1768 Merge Strings Alternately, Easy, Strings

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        w = []
        
        for i in range(min(len(word1), len(word2))):
            w.append(word1[i])
            w.append(word2[i])
        
        w.extend(word1[len(word2):])
        w.extend(word2[len(word1):])

        return "".join(w)