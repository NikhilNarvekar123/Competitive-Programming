'''
O(n) runtime
O(1) mem
'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        if not fast:
            return slow
        else:
            return slow.next
        
