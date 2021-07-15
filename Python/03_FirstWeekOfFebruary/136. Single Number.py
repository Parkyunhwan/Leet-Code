class Solution:
    # xor의 마법으로 두번 나오게 되면 1 1 -> 0이 되게 된다.
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result