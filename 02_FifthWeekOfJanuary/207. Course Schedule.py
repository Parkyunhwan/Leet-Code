class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # defaultdict 순회 문제 시 전혀 값을 건들지 않았는데 값을 바꿨다고 나올 수 있다.
        # 그 이유는 defaultdict가 빈 값 조회시 null말고 디폴트를 생성하므로 나는 오류이다.
        graph = collections.defaultdict(list)


        for x, y in prerequisites:
            graph[x].append(y)

        traced = set() # 중복 노드를 검사해서 사이클을 검사하는 집합
        visited = set() # 이미 방문한 즉, 이미 검증된 노드를 기록하는 집합
        # visited로 가지치기가 가능해져 속도의 엄청난 향상을 가져옴.

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]: # 빈 값 조회시 빈 리스트가 생성되긴 한다. 따라서 딕셔너리가 바뀌는 것이다.
                if not dfs(y):
                    return False
            traced.remove(i)

            visited.add(i)
            return True

        for x in list(graph):
            print(x)
            if not dfs(x):
                return False

        return True

