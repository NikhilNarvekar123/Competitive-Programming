class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        
        if(dividend == -pow(2,31) and divisor == -1):
            return (pow(2,31) - 1)
        
        sign = 1
        if(dividend >= 0) == (divisor >= 0):
            sign = 1
        else:
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        count = 0
        
        while(dividend - divisor >= 0):
            pwr = 0
            while(dividend - (divisor << 1 << pwr) >= 0):
                pwr += 1
            count += 1 << pwr
            dividend -= divisor << pwr
        
        return int(sign * count)
        
        
        '''
        if(dividend == -pow(2,31) and divisor == 1):
            return -pow(2,31)
        if(dividend == -pow(2,31) and divisor == -1):
            return pow(2,31) - 1
        if(dividend == pow(2,31) - 1 and divisor == 1):
            return pow(2,31) - 1
        if(dividend = pow(2,31) - 1 and divisor == -1):
            return -(pow(2,31) -1)
        
        count = 0
        
        sign = 1
        if(dividend < 0 and divisor < 0):
            sign = 1
        elif(dividend < 0 and divisor > 0):
            sign = -1
        elif(dividend > 0 and divisor < 0):
            sign = -1
        
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        
        while((dividend - divisor) >= 0):
            dividend -= divisor
            count += 1
         
        return sign * count
        '''
