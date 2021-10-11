'''
run-time: 47 ms (faster than 30.64%)
mem-usage: 14.2 mb (less than 60.99%)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        i = j = 0
        res = ListNode()
        dummy = res
        
        while l1 and l2:
            
            if l1.val > l2.val:
                dummy.next = ListNode(l2.val, None)
                l2 = l2.next
            else:
                dummy.next = ListNode(l1.val, None)
                l1 = l1.next

            dummy = dummy.next

        dummy.next = l1 or l2
            
        return res.next
                
