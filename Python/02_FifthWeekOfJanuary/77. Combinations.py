# itertools 모듈이 비교가 안되게 훨씬 빠름!
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1, n + 1)]
        return list(itertools.combinations(arr, k))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1, n + 1)]
        def dfs(index):
            if len(tmp) == k:
                result.append(tmp[:])
                return
            for i in range(index, n):
                tmp.append(arr[i])
                dfs(i + 1)
                tmp.pop()
        result = []
        tmp = []
        dfs(0)
        return result