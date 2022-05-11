"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        sum = 0
        weight = 1
        while l1 != None:
            num1 += l1.val*weight
            weight = 10*weight
            l1 = l1.next
        weight = 1
        while l2 != None:
            num2 += l2.val*weight
            weight = 10*weight
            l2 = l2.next
        sum = num1+num2

# note below
        sum= str(int(num1)+int(num2))
        i= len(sum)-1
        output= ListNode(int(sum[i]))
        next= output
        while i:          
            i-=1
            ch= int(sum[i])
            if next != None:
                next.next= ListNode(ch)          
                next= next.next
                
        return output
            