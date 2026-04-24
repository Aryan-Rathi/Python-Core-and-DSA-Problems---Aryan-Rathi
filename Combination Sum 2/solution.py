class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        
        def backtrack(remain, curr_comb, start):
            if remain == 0:
                res.append(list(curr_comb))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remain:
                    break
                
                curr_comb.append(candidates[i])
                backtrack(remain - candidates[i], curr_comb, i + 1)
                curr_comb.pop()
        
        backtrack(target, [], 0)
        return res
