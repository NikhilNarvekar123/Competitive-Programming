class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        rez = []
        candidates.sort()
        self.dfs(candidates, 0 , target, [], rez)
        return rez
        
        
    def dfs(self, candidates, idx, target, current : List[int], rez):
        
        if target == 0:
            temp = current.copy()
            rez.append(temp)
            return
        if target < 0:
            return
        
        for i in range(idx, len(candidates)):
            if(i == idx or candidates[i] != candidates[i-1]):
                current.append(candidates[i])
                self.dfs(candidates, i + 1, target - candidates[i], current, rez)
                current.pop(-1)
        
        
