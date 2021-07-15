class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = dict()
        for jewel in jewels:
            dic[jewel] = 0

        for stone in stones:
            if dic.get(stone) is not None:
                dic[stone] += 1
        return sum(dic.values())

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0
        for jewel in jewels:
            count += freqs[jewel]
        return count
