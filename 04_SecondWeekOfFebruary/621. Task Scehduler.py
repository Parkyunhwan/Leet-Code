# max heap을 사용한 코드 중 그나마 이해하기 쉬운 코드.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = [-i for i in collections.Counter(tasks).values()] # task의 갯수를 key로하는 min list를 만들고
        heapq.heapify(c) # heapfiy를 통해 리스트의 힙화
        count = 0

        while len(c)>0: # 힙이 비어있지 않다면 계속
            temp = []
            i=0
            # n초가 넘기전 그리고 ( 힙 또는 (재사용 가능 task가 있을 때) )
            while i<=n and (len(c)>0 or len(temp)>0):
                count += 1

                # 힙에 아직 사용하지 않은 태스크가 있는가? -> 없다면 idle로 count만 증가
                if len(c) > 0:
                    # 남은 횟수가 많은 task부터 빠져 나옴
                    t = -heapq.heappop(c)-1

                    # 아직도 태스크 횟수가 남아 있다면 재사용 가능 리스트에 넣어둠
                    if t > 0:
                        temp.append(t)
                # 제한 시간 계산 용
                i += 1
            for i in temp:
                heapq.heappush(c,-i)
        return count


'''

Example explanation:

tasks = ["A","A","A","B","B","B"], n = 2

Procedure:

1.
# Build a dictionary for tasks
# key   : task
# value : occurrence of task

max_occ = 3

number_of_taks_of_max_occ = 2 with {'A', 'B'}

2.
#Make (max_occ - 1) = 2 groups, groups size = n+1 = 3
#Fill each group with uniform iterleaving as even as possible

group = '_ _ _' with size = 3

=> make 2 groups with uniform iterleaving

A B _ A B _

3.
# At last, execute for the last time of max_occ jobs

A B _ A B _ A B


length of task scheduling with cooling = 8

'''

from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            # Quick response for special case on n = 0
            # no requirement for cooling, just do those jobs in original order
            return len(tasks)

        # key   : task
        # value : occurrence of tasks
        task_occ_dict = Counter(tasks)

        # max occurrence among tasks
        max_occ = max(task_occ_dict.values())

        # number of tasks with max occurrence
        number_of_taks_of_max_occ = sum((1 for task, occ in task_occ_dict.items() if occ == max_occ))

        # Make (max_occ-1) groups, each groups size is (n+1) to meet the requirement of cooling
        # Fill each group with uniform iterleaving as even as possible

        # At last, execute for the last time of max_occ jobs
        intervl_for_schedule = (max_occ - 1) * (n + 1) + number_of_taks_of_max_occ

        # Minimal length is original length on best case.
        # Otherswise, it need some cooling intervals in the middle
        return max(len(tasks), intervl_for_schedule)
