# Leetcode 735 Asteroid Collision, Stack

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a) == stack[-1]:
                    stack.pop()
                    break
                elif abs(a) < stack[-1]:
                    break
                
            else:
                stack.append(a)
        return stack
        
# Time Complexity O(n)