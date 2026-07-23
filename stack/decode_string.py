# 394 Decode String, Stack

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                
                stack.pop() 
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                decoded_segment = int(k) * substring
                stack.append(decoded_segment)
                
        return "".join(stack)

# Time Complexity O(n)