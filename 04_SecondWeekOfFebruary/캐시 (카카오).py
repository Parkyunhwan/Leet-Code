import collections


def solution(cacheSize, cities):
    q = collections.deque()
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if not q:
            q.append(city)
            answer += 5
        else:
            if not city in q:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(city)
                answer += 5
            else:
                q.remove(city)
                q.append(city)
                answer += 1

    return answer