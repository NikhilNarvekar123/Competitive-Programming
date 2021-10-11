'''
run-time: 72 ms (faster than 59.47%)
mem-usage: 17.1 mb (better than 67.25%)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
            
        if head == None:
            return None
        
        dummy = head
        prev = None
        
        while dummy != None:
            
            if dummy.val == val and prev != None:
                prev.next = dummy.next
                dummy.next = None
                dummy = prev.next            
            elif dummy.val == val:
                head = dummy.next
                dummy.next = None
                dummy = head
            else:
                prev = dummy
                dummy = dummy.next    
        
        return head
            
            
