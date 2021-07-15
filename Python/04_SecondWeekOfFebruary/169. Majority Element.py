# My Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

# book => 내가 잘 안 쓰는 리스트의 count메서드를 사용해서 해결 (타임 아웃 ㅠㅠ)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

# book -> 간단한 메모제이션..
class Solution:
    # 한 번 기록된 값은 메모제이션을 통해 계산량이 큰 nums.count 를 계산하지 않고 조건 검사 가능
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2
                return num