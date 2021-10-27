'''
run-time: 64 ms (faster than 48.69%)
mem-usage: 14.2 mb (less than 96.42%)
'''

from queue import PriorityQueue

class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
    
    
        freqMap = {}
        
        
        for word in words:
            if word in freqMap:
                freqMap[word] -= 1
            else:
                freqMap[word] = -1
                
        
        q = PriorityQueue()
        
        for key, val in freqMap.items():
            q.put((val, key))
        
        res = []
        for i in range(k):
            res.append(q.get()[1])
            
        return res
