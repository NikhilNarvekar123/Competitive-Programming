'''
run-time: 44ms, faster than 99.52%
mem-usage: 13.2 MB, less than 99.06%
'''

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
        
        carry = 0
        resultSum = ListNode()
        tempSum = resultSum # reference to keep adding to result linked list
        
        while l1 or l2:
            
            digitSum = carry
            carry = 0
            
            if l1:
                digitSum += l1.val
                l1 = l1.next
            
            if l2:
                digitSum += l2.val
                l2 = l2.next
                
            if digitSum >= 10:
                carry = 1
                digitSum -= 10
            
            tempSum.val = digitSum
            if l1 or l2:
                tempSum.next = ListNode()
                tempSum = tempSum.next
                
        if carry == 1:
            tempSum.next = ListNode(1, None)
        
        return resultSum
