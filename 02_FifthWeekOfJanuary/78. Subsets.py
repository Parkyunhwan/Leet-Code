# My Solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, limit):
            if limit == index:
                result.append(tmp[:])
                return
            for i in range(index, len(nums)):
                tmp.append(nums[i])
                dfs(i + 1, limit)
                tmp.pop()

        result = []
        for limit in range(len(nums) + 1):
            tmp = []
            dfs(0, limit)

        return result

# 책 풀이 -> 나올 수 있는 모든 경우가 부분 집합이므로 모두 result에 저장한다.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        result = []
        dfs(0, [])
        return result