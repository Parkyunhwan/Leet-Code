class Solution:
    '''
    가장 큰 값을 내는 최장 길이 서브 배열을 구하는 문제
    1. 가장 큰 값을 내야한다.
    2. 연속된 배열이여만 한다.

    따라서, 누적합이 음수가 된 값은 이어가면 손해이므로 이어갈 필요가 없다. -> 그냥 처음 부터 시작한다는 의미로 누적합을 0으로 주고 현재값부터 다시 시작
    각 인덱스 별 누적합을 모두 기록해두고 마지막에 그 중 가장 큰 값을 리턴
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        return max(sums)

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)