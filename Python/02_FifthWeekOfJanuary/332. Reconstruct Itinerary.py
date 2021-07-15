# global 변수를 쓸 때 여러 테스트 케이스를 하게 되면 테스트 케이스가 겹칠수 있으므로 오류에 굉장히 민감하므로 주의가 필요하다.
# My Solution
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(itinerary, ret):
            if len(itinerary) == len(tickets) + 1:
                ret = itinerary[:]
                return ret

            departure = itinerary[-1]
            for idx, arrival in enumerate(dic[departure]):
                dic[departure].pop(idx)
                ret = dfs(itinerary + [arrival], ret)
                dic[departure].insert(idx, arrival)
                if ret:
                    break
            if ret:
                return ret

        dic = collections.defaultdict(list)

        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])

        for key in dic.keys():
            dic[key].sort()
        result = ["JFK"]
        ret = []
        ret = dfs(result, ret)
        return ret

