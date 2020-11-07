# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        if head == None or head.next == None:
            return None

        
        length = 1 
        temp2 = head
        
        while temp2.next != None:
            temp2 = temp2.next
            length += 1

        rotateTimes = k % length

        if k == 0 or rotateTimes == 0:
            return head

        fastPointer = head
        slowPointer = head

        for a in range (rotateTimes):
            fastPointer = fastPointer.next


        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        temp = slowPointer.next

        slowPointer.next = None
        fastPointer.next = head
        head = temp

        return head
    
        '''
    
        if head == None or head.next == None:
            return head
    
        length = 1 
        temp2 = head
        while temp2.next != None:
            temp2 = temp2.next
            length += 1
        
    
        for n in range(0, k % length):
            
            temp = head
            
            while temp.next.next != None:
                temp = temp.next
            
            temp.next.next = head
            head = temp.next
            temp.next = None
            
        return head
    
    
