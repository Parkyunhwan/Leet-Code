# my solution 산 상태와 판 상태 두가지로 나눠서 계산을 했는데 무제한 거래가 가능하므로 조건을 더욱 간단하게 만들 수 있었다.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        status = 0 # 0 is buy , 1 is sell
        amount = 0
        profit = 0
        for i in range(len(prices) - 1):
            curr = prices[i]
            future = prices[i + 1]
            if status == 0 and future > curr:
                status = 1
                amount = prices[i]
            elif status == 1 and future < curr:
                profit += prices[i] - amount
                amount = 0
                status = 0
        if status == 1:
            profit += prices[len(prices) - 1] - amount
        return profit

# book solution
# 다음번에 오른다며 매번 살 때마다 미리 이득을 계산해둔다. 오를 때마다 거래를 해서 계산한다. (무제한 거래)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) -1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result