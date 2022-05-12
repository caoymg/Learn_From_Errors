"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        best = 0
        current_index = {}
        for tail in range(len(s)):
            if s[tail] in current_index:
                # we can skip the characters immediately when we found a repeated character.
                # The reason is that if s[j] have a duplicate in the range [i, j) with index j', 
                # we don't need to increase i little by little. 
                # We can skip all the elements in the range [i, j'] and let i to be j' + 1 directly.
                head = max(current_index[s[tail]], head)
                    
            best = max(best, tail-head+1)
            current_index[s[tail]]=tail+1
                
        return best
                
"""
solution 2

"no repeat" make me think of "set"

#  note different cases
        if len(s)>0:
            best = 1
        else:
            best = 0
            
        for i in range(len(s)):
# note where to put initialization
            no_repeat_lst = []
            no_repeat_lst.append(s[i])
            for j in range(i+1,len(s)):
                old = len(set(no_repeat_lst))
                no_repeat_lst.append(s[j])
                new = len(set(no_repeat_lst))
                if old < new:
                    record = len(set(no_repeat_lst))
                    if record > best:
                        best = record
                else:
                    break
                    
        return best
                    
""" 