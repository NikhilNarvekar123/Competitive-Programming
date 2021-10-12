class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        l = s.split()
        if len(l)!=len(pattern):
            return False
        d={}
        idx=0
        for i in pattern:
            if i not in d and l[idx] not in d.values():
                d[i]=l[idx]
            elif i not in d and l[idx] in d.values():
                return False
            
            elif i in d:
                if d[i]!=l[idx]:
                    return False
            idx += 1
        return True
