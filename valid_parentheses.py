'''
run-time: 32 ms (faster than 72.57%)
mem-usage: 14.3 mb (less than 64.44%)
O(n)
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        charDict = {'}': '{', ']' : '[', ')': '('}
        
        for c in s:
            if len(stack) != 0:
                old = stack.pop()
                if c in charDict and charDict[c] == old:
                    continue
                stack.append(old)
                stack.append(c)
            else:
                stack.append(c)
        
        return len(stack) == 0
