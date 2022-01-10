'''
O(n/2)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        next = head.next
        head.next = next.next
        next.next = head
        
        head.next = self.swapPairs(head.next)
        return next
