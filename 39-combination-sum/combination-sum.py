class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        stack = [(0,0,[])]
        while stack:
            index, total, cand = stack.pop()

            if total == target:
                ans.append(cand)
            elif total > target or index == len(candidates):
                continue
            else:
                stack.append((index,total+candidates[index],cand+[candidates[index]]))
                stack.append((index+1,total,cand))
        return ans


        # ans = []
        # cur = []
        # def dfs(i, total):
        #     if total == target:
        #         ans.append(cur.copy())
        #         return
        #     if i == len(candidates) or total > target:
        #         return
        #     cur.append(candidates[i])
        #     dfs(i,total+candidates[i])
        #     cur.pop()
        #     dfs(i+1,total)
        #     return
        # dfs(0,0)
        # return ans