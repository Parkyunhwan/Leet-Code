# in과 딕셔너리를 통한 풀이 방법
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return nums_map[target - num], i
            nums_map[num] = i