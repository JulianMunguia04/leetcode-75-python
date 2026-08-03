# 242 Valid Anagram, Hashmap

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        h1 = {}
        h2 = {}

        if len(s) != len(t):
          return False

        for i in range(len(s)):
          if s[i] in h1:
            h1[s[i]] += 1
          else: 
            h1[s[i]] = 1
          
          if t[i] in h2:
            h2[t[i]] += 1
          else: 
            h2[t[i]] = 1
        
        print(h1, h2)
        return h1 == h2