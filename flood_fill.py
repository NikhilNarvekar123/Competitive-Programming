class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        og_color = image[sr][sc]
        image[sr][sc] = color
        
        queue = deque()
        queue.append((sr, sc))
        visited = set()
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(queue):
            r, c = queue.popleft()
            visited.add((r, c))
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr >= 0 and nr < len(image) and nc >= 0 and nc < len(image[0]):
                    if not ((nr, nc) in visited) and image[nr][nc] == og_color:
                        image[nr][nc] = color
                        queue.append((nr, nc))
        
        return image
