# 1456. Maximum Number of Vowels in a Substring of Given Length, Sliding Window

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = {"a","e","i","o","u"}
        vowelCount = 0
        windowString = ""

        for i in range(k):
          windowString += s[i]
          if s[i] in vowels:
            vowelCount += 1

        maximum = vowelCount
        for i in range(1, len(s) - k+1):
          if s[i+k-1] in vowels:
            vowelCount += 1

          if s[i-1] in vowels:
            vowelCount -= 1

          windowString = windowString[1:]
          windowString += s[i+k-1]
          
          maximum = max(maximum, vowelCount)
        
        return maximum