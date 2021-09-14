def firstDuplicate(a):
  
    indexSet = {}
    
    for i in range(len(a)):
        if a[i] in indexSet:
            return a[i]
        else:
            indexSet[a[i]] = i
      
    return -1
