# O(n^2)의 가장 기본적인 풀이
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            g, c = gas[start], cost[start]
            if g >= c:
                remain = 0
                for i in range(len(gas)):
                    idx = (start + i) % len(gas)
                    remain += gas[idx]
                    curr_cost = cost[idx]
                    if remain < curr_cost:
                        remain -= curr_cost
                        break
                    else:
                        remain -= curr_cost
                if remain >= 0:
                    return start
        return -1

# O(n)에 문제 이해를 넘어 국어를 파괴해버림
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 수학적 귀류법? 을 이용한 증명 답은 분명히 하나 존재한다고 했으므로
        # 먼저 답이 없는 경우를 처리한다.
        # 이후에는 무조건 답이 하나 존재하므로 만약 안되는 지점이 발견되면 그 다음 지점이 답이 될 확률이 있다.
        # 그렇게 한 바퀴를 돌아 마지막에 설정된 지점이 시작 지점이 된다.
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
