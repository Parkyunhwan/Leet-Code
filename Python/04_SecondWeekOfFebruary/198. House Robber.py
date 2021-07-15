class Solution:
    def rob(self, nums: List[int]) -> int:
        mx = 0
        n = len(nums)
        nums = [0] + nums
        dp = [0] * (n + 1)
        if n <= 2:
            return max(nums)
        dp[1], dp[2] = nums[1], nums[2]
        mx = max(dp[1], dp[2])
        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
            # dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            mx = max(dp[i], mx)
        return mx


class Solution:
    def rob(self, nums: List[int]) -> int:
        mx = 0
        n = len(nums)
        dp = [0] * n
        if not nums:
            return 0
        if n < 2:
            return max(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        mx = max(dp[1], dp[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            mx = max(dp[i], mx)
        return mx
