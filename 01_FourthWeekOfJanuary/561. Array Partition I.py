class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = 0
        for i in range(0, len(nums), 2):
            sm += nums[i]
        return sm

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])