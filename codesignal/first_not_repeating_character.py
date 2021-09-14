def firstNotRepeatingCharacter(s):

    characMap = {}
    repeatSet = set()
    
    for i in range(len(s)):
        if s[i] in characMap:
            repeatSet.add(s[i])
            characMap.pop(s[i])
        elif not (s[i] in repeatSet):
            characMap[s[i]] = i
    
    minCharac = '_'
    minIdx = -1
    
    for charac, idx in characMap.items():
        if idx < minIdx or minIdx == -1:
            minIdx = idx
            minCharac = charac
    
    return minCharac
