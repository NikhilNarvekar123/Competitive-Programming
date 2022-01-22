'''
O(log n)
log n since number has log n digits, and have to loop for that many digits
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seenNums = set()
        
        while True:
            sum = 0
            while n != 0:
                sum += (n % 10) ** 2
                n = n // 10
            if sum == 1:
                return True
            elif sum in seenNums:
                return False
            else:
                seenNums.add(sum)
                n = sum
