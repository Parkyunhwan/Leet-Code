class Solution:
    '''
        만약, while start < end: 이면
        nums 갯수가 2개일 때와 1개일 때 오류가 발생하게 된다.
        또한 start와 end가 같아지는 경우를 처리하지 못하게 된다.
    '''
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


class Solution:
    '''
        재귀
    '''
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    return binary_search(left, mid - 1)
                elif nums[mid] < target:
                    return binary_search(mid + 1, right)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

'''
    bisect는 타겟 숫자가 위치한 인덱스를 반환한다.
    하지만 타켓 숫자가 없다면 그 사이에 있는 인덱스를 반환한다.
    또한, 타겟 숫자가 가장 작은 수보다 작다면 0을 반환하고 가장 큰 수보다 크다면 가장 큰 수 + 1 인덱스를 반환한다.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
