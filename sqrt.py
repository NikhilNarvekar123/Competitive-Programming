class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        j = x
        num = 0
        
        while(i <= j):
            mid = (i + j) // 2
            if(mid * mid > x):
                j = mid - 1
            elif(mid * mid < x):
                i = mid + 1
                num = mid
            else:
                return mid
            
            
        return num
        
        
        '''
        return(int(pow(x, 1/2)))
        '''
