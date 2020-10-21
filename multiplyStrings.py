class Solution:
    def multiply(self, num1: str, num2: str) -> str:
   

        











'''


        base = 1
        sum1 = 0
        for d in reversed(num1):
            sum1 += base * int(d)
            base *= 10
            
            
        base = 1
        sum2 = 0
        for d in reversed(num2):
            sum2 += base * int(d)
            base *= 10
        
               
        return str(sum1 * sum2)
        
        '''

        base = 1
        sum1 = 0
        
        for i in range(len(num1) - 1, -1, -1):
            
            d = num1[i]
            digit = 0
            
            if d == "1":
                digit = 1
            elif d == "2":
                digit = 2
            elif d == "3":
                digit = 3
            elif d == "4":
                digit = 4
            elif d == "5":
                digit = 5
            elif d == "6":
                digit = 6
            elif d == "7":
                digit = 7
            elif d == "8":
                digit = 8
            elif d == "9":
                digit = 9
            
        
            sum1 += digit * base
            base *= 10
        
        base = 1
        sum2 = 0
        
        for i in range(len(num2) - 1, -1, -1):
            
            d = num2[i]
            digit = 0
            
            if d == "1":
                digit = 1
            elif d == "2":
                digit = 2
            elif d == "3":
                digit = 3
            elif d == "4":
                digit = 4
            elif d == "5":
                digit = 5
            elif d == "6":
                digit = 6
            elif d == "7":
                digit = 7
            elif d == "8":
                digit = 8
            elif d == "9":
                digit = 9
            
        
            sum2 += digit * base
            base *= 10
        
        
        
        return str(sum1 * sum2)
            
