# 2390 Removing Stars from a String

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        
        for char in s:
            if not char == "*":
                stack.append(char)
            else:
                stack.pop()
        
        string = ""

        for char in stack:
            string += char
            
        return string
        
# Time Complexity O(n)


