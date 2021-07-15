
# 타뷸레이션 상향식 풀이 (28ms)
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# 가장 느린 브루트포스 풀이 (788ms)
# n부터 n - 1 , n - 2
# 중복되는 하위 값을 중복계산하기 때문에 시간이 오래 걸림
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# 브루트포스 방식을 개선 한 메모제이션 방식
# 이미 계산한 하위 문제들을 계산하지 않음으로써 시간을 절약
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n < 2:
            return n

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[N]