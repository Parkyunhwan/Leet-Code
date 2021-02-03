# Book Solution
'''
전형적인 소팅 문제이나 하나의 키 값으로 소팅하는 문제가 아니였다.
어떤 키값으로 소팅을 할지가 중요한 문제
여기서는 키 값으로 비교할 두 원소를 더한 값이였다 1. a + b, 2. b + a
리턴 값을 str(int())로 감싸주는 이유는 입력값이 [0, 0] 일 때 00 이 아닌 0을 반환하기 위한 처리이다. (''.join() 사용 시 주의점)
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def check_swap(a, b):
            return str(a) + str(b) < str(b) + str(a) # 스왑 한 경우가 더 큰 경우 (True 반환)
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and check_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1
        return str(int(''.join(map(str,nums))))