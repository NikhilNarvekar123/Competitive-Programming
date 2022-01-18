'''
O(n)
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Two-pointer (O(n))
        slow = fast = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        
        # recursive solution O(n)
        '''
        global cnt
        cnt = n
        
        def recur(node):
            global cnt
            if not node:
                cnt -= 1
                return None
            
            node.next = recur(node.next)
            
            cnt -= 1
            if cnt == -1:
                return node.next
            else:
                return node

        return recur(head)
        '''
