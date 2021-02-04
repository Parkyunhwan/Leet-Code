class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left <= right:
            sm = numbers[left] + numbers[right]

            if sm < target:
                left += 1
            elif sm > target:
                right -= 1
            else:
                return [left + 1, right + 1]
