# 저점과 현재값과의 차이 계산
# O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit


# O(n^2) -> 브루트포스
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                buy = prices[i]
                sell = prices[j]
                if sell - buy > 0:
                    profit = max(profit, sell - buy)
        return profit