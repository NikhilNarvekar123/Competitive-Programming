def rotateImage(a):

    n = len(a)
    
    for r in range(n):
       
        for c in range(r + 1, n):
            temp = a[r][c]
            a[r][c] = a[c][r]
            a[c][r] = temp
        
        a[r].reverse()
    
    return a
