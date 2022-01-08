'''
run-time: 86 ms, faster than 17.27%
mem-usage: 14.5 mb, less tham ?
O(n)
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        doubles = set()
        for i in range(len(arr)):
            if arr[i] * 2 in doubles or arr[i] / 2 in doubles:
                return True
            else:
                doubles.add(arr[i])
        
        return False
