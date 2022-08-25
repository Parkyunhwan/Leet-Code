from collections import deque
import heapq
def solution(jobs):
    answer = 0
    sorted_jobs = deque(sorted([[job[1], job[0]] for job in jobs], key = lambda x : (x[1], x[0])))

    heapq.heappush(q, sorted_jobs.popleft())
    current_time = 0
    total_time = 0
    while q:
        duration, arrive = heapq.heappop(q)
        current_time = max(current_time + duration, arrive + duration)
        total_time += current_time - arrive
        while len(sorted_jobs) > 0 and current_time > sorted_jobs[0][1]:
            heapq.heappush(q, sorted_jobs.popleft())
        if len(sorted_jobs) > 0 and len(q) == 0:
            heapq.heappush(q, sorted_jobs.popleft())
    return total_time // len(jobs)