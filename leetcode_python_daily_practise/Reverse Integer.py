
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        tmp = 0
        weight = 1
        sign = 0
        for i in range(len(x_str)): 
            if x_str[i] == "-":
                sign = 1
            else:
                tmp += int(x_str[i])*weight
                weight =  weight*10
        # Note the usage of math.pow(base, exponent)
        if tmp > math.pow(2, 31)-1 or tmp < -math.pow(2, 31):
            out = 0
        else:
            out = tmp
            
        if sign:
            return -out
        else:
            return out
        
            
                    
                    