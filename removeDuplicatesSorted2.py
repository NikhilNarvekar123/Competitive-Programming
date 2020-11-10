# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        

        tempNode = head
        prevPtr = tempNode
        vals = []
        skipped = False
        
        while tempNode != None:
            
            tempNode = tempNode.next
            
            if (not tempNode):
                if not skipped:
                    vals.append(prevPtr.val)
                continue
            
            if prevPtr.val != tempNode.val:
                if not skipped:
                    vals.append(prevPtr.val)
                    prevPtr = prevPtr.next
                else:
                    skipped = False
                    prevPtr = tempNode
            else:
                skipped = True
                
            
        newHead = None
        prevNode = newHead
        
        for n in vals:
            newNode = ListNode(n)
            
            if(newHead == None):
                newHead = newNode
            else:
                prevNode.next = newNode
            
            prevNode = newNode
        
        return newHead  
            
        
        
        
        
        
        '''
        vals = []
        toRemove = []
        temp = head
        
        while temp != None:
            
            if temp.val in vals and not (temp.val in toRemove):
                toRemove.append(temp.val)
            elif not (temp.val in vals):
                vals.append(temp.val)
            temp = temp.next
        
        print(vals)
        for n in toRemove:
            vals.remove(n)

        newHead = None
        prevNode = newHead
        
        for n in vals:
            newNode = ListNode(n)
            
            if(newHead == None):
                newHead = newNode
            else:
                prevNode.next = newNode
            
            prevNode = newNode
        
        return newHead
        '''
