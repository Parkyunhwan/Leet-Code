# My solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            if len(tmp) == len(nums):
                cp = tmp[:] # 파이썬의 객체 참조 특성으로 인해 꼭 복사를 해줘야 한다.
                result.append(cp)
                return
            for i in range(len(nums)):
                if nums[i] not in tmp:
                    tmp.append(nums[i])
                    dfs(i + 1)
                    tmp.pop()
        result = []
        tmp = []
        dfs(0)
        print(result)
        return result

# Book Solution (리스트에서 값을 제외시키면서 체크하는 방법)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e) # 넘어온 요소에서 넣을 요소를 제외시켜서 중복 체크를 진행한다.

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        result = []
        prev_elements = []
        dfs(nums)
        return result