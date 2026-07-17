# 1071 Greatest common divisor of strings

import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        gcd = ""

        if not str1 + str2 == str2+str1:
            return ""

        gcd_length = math.gcd(len(str1), len(str2))

        for i in range(gcd_length):
            gcd += str1[i]
        
        #or simply return str[:gcd_length]
        
        return gcd

#Time Complexity O(n + m)