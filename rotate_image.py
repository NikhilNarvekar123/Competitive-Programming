class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose
        n = len(matrix)
        i = [0,0]
        
        while i != [n, n]:
            for offset in range(n - i[0]):
                j = [i[0] + offset, i[1]]
                k = [i[0], i[1] + offset]
                matrix[j[0]][j[1]], matrix[k[0]][k[1]] = matrix[k[0]][k[1]], matrix[j[0]][j[1]]
            i[0] += 1
            i[1] += 1
        
        # reflect
        for row in matrix:
            j = 0
            k = n - 1
            while j < k:
                row[j], row[k] = row[k], row[j]
                j += 1
                k -= 1
            
