class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        '''
        pwr = 1
        num = 0
        for i in range(len(digits) - 1, -1, - 1):
            num += digits[i] * pwr
            pwr *= 10
        
        num += 1
        
        temp = []
        while(num != 0):
            temp.insert(0, num % 10)
            num = num // 10
        
        return temp
        '''
        
    
        idx = 0
        self.helper(digits, 0)
        return digits
    
    def helper(self, digits: List[int], idx : int):
        
        if(idx >= len(digits)):
            digits.insert(0,1)
            return
        digit = digits[-1 - idx]
        if digit != 9:
            digits[-1 - idx] += 1
        else:
            digits[-1 - idx] = 0
            idx += 1
            self.helper(digits, idx) 
