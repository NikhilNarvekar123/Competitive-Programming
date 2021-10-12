'''
run-time: 32 ms (faster than 99.19%)
mem-usage: 15 mb (less than 89.73%)
'''

class Solution:
    
    def fizzBuzz(self, n: int) -> List[str]:
    
        arr = []
        
        for i in range(1, n + 1):
            
            if i % 3 == 0 and i % 5 == 0:
                arr.append('FizzBuzz')
            elif i % 3 == 0:
                arr.append('Fizz')
            elif i % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(str(i))
        
        return arr
