'''
run-time: 158 ms (faster than 23.62%)
mem-usage: 19 mb (less than 19.65%)

O(n log n) solution
'''

from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        intMap = {}
        
        for num in nums:
            if num in intMap:
                intMap[num] -= 1
            else:
                intMap[num] = -1
        
        
        q = PriorityQueue()
        
        for key, value in intMap.items():
            q.put((value, key))
            
        res = []
        
        for i in range(k):
            res.append(q.get()[1])
        
        return res
