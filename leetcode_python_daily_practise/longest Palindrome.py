"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = ""
        for head in range(len(s)):
            tail = len(s)-1
            while tail > head:
                if s[tail] == s[head]:
                    flg = 1
                    temp_sub_s = s[head:tail+1]
                    for i in range(len(temp_sub_s)):
                        if i < len(temp_sub_s)-i:
                            if temp_sub_s[i] !=temp_sub_s[len(temp_sub_s)-i-1]:
                                flg = 0
                    if flg==1:
                        if len(temp_sub_s)>len(best):
                            best = temp_sub_s
                tail -= 1
        
        if len(best) ==0:
            return s[0]
                
        return best
                    

                    
                    