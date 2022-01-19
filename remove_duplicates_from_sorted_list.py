'''
O(n)
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        dummy = head.next
        prev = head
        
        while dummy != None:
            if dummy.val == prev.val:
                prev.next = dummy.next
                dummy = dummy.next
            else:
                prev = dummy
                dummy = dummy.next
        
        return head
