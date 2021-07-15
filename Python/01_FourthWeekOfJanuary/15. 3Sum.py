class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sm = nums[i] + nums[left] + nums[right]
                if sm < 0:
                    left += 1
                elif sm > 0:
                    right -= 1
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    ret.append(temp)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return ret