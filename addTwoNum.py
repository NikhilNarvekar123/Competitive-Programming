# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
   

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        fin = ListNode()
        l3 = fin
        carry = 0
        firstLoop = True
        
        while l1 != None or l2 != None:
            
            num1 = l1.val if l1 != None else 0
            num2 = l2.val if l2 != None else 0
            l1 = l1.next if l1 != None else None 
            l2 = l2.next if l2 != None else None
            
            numSum = num1 + num2 + carry
            
            carry = numSum // 10
            
            l3.next = ListNode(numSum % 10, None)
            l3 = l3.next
            if firstLoop:
                fin = l3
                firstLoop = False
        
        if carry != 0:
            l3.next = ListNode(1, None)
            l3 = l3.next
        
        return fin


    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = ""
        num2 = ""
        finNum = 0
        
        while l1 != None:
            num1 = str(l1.val) + num1
            l1 = l1.next 
        
        while l2 != None:
            num2 = str(l2.val) + num2
            l2 = l2.next 
        
        finNum = int(num1) + int(num2)
        
        tempStr = str(finNum)
        
        l1 = ListNode(int(tempStr[len(tempStr) - 1]), self.recur(2, tempStr))  
            
        return l1
    
    
    def recur(self, val, tempStr) -> ListNode:
        if(len(tempStr) - val >= 0):
            return ListNode(int(tempStr[len(tempStr) - val]), self.recur(val + 1, tempStr))
            
    '''
