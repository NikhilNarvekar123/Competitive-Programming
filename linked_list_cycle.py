'''
O(n)
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
