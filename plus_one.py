'''
run-time: 72 ms (faster than 5.02%)
mem-usage: 14.1 mb (less than 74.24%)
best-case: O(1), worst-case: O(n)
'''
class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
    
        i = len(digits) - 1
        
        if digits[i] < 9:
            digits[i] += 1
        else:

            while digits[i] == 9:
                digits[i] = 0
                i -= 1

            if i >= 0:
                digits[i] += 1
            else:
                digits.insert(0,1)
        
        return digits
