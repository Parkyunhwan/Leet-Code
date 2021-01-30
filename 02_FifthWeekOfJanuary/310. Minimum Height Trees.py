class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:  # 2개 남았을 땐 서로가 리프노드가 되므로 반복문을 빠져나온다.
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()  # 1개 연결되있던 노드를 빼서 다음 조건 노드로 선택한다.
                graph[neighbor].remove(leaf)  # 일단 리프노드를 제외시킨다.

                if len(graph[neighbor]) == 1:  # 다음 조건 노드의 값의 갯수가 1인지(리프노드) 검사한다.
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
