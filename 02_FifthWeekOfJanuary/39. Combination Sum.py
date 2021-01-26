# My Solution (중복 조합)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index):
            sm = sum(tmp)
            if sm > target:
                return
            if sm == target:
                result.append(tmp[:])
                return
            for i in range(index, len(candidates)):
                tmp.append(candidates[i])
                if sum(tmp) <= target:
                    dfs(i) # 중복으로 선택할 수 있게 현재 선택한 인덱스를 넘긴다. 그 후에도 중복 선택이 가능하게 된다.
                           # 만약 i 가 아닌 0을 입력하게 되면 중복 순열이 될 것이다.
                tmp.pop()

        result = []
        tmp = []
        dfs(0)
        return result