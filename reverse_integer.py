'''
run-time: 28 ms, faster than 90.73%
mem-usage: 14.2 mb, less than 46.27%
O(n)
'''

class Solution:
    def reverse(self, x: int) -> int:
           
        intMax = (2 ** 31) - 1
        intMin = (2 ** 31)
        flag = False
        res = 0
        
        if x < 0:
            flag = True
            x *= -1
        
        while x != 0:
            digit = x % 10
            x = x // 10
            if (not flag) and intMax // 10 < res or (res == intMax // 10 and intMax % 10 < digit):
                return 0
            elif (flag) and intMin // 10 < res or (res == intMin // 10 and intMin % 10 < digit):
                return 0
            res = (res * 10) + digit
        
        return (res * -1) if flag else res 
