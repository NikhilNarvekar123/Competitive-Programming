class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        rez = {}
        
        for str in strs:
            temp = []
            for c in str:
                temp.append(c)
            temp.sort()
            
            if tuple(temp) in rez:
                rez[tuple(temp)].append(str)
            else:
                rez[tuple(temp)] = [str]
        
        return rez.values()
        '''
        
        
        
        rez = {}
        
        for str in strs:
            
            totalHash = 0
            for c in str:
                totalHash += hash(c)
            
            if totalHash in rez:
                rez[totalHash].append(str)
            else:
                rez[totalHash] = [str]
        
        return list(rez.values())
        
        
        '''
        rez = {}
        
        for str in strs:
            charCount = [ 0 for i in range(26)]
            
            for c in str:
                charCount[ord(c) - ord('a')] += 1
            
            if(tuple(charCount) in rez):
                rez[tuple(charCount)].append(str)
            else:
                rez[tuple(charCount)] = [str]
        
        return rez.values()
        '''
