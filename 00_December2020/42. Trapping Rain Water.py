# 투 포인터 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        rain = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                rain += left_max - height[left]
                left += 1
            else:
                rain += right_max - height[right]
                right -= 1
        return rain