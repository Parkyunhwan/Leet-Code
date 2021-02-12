import collections


def solution(m, n, board):
    answer = 0
    count = 1
    board = [list(b) for b in board]
    while count != 0:
        check = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m - 1):
            for j in range(n - 1):
                p = board[i][j]
                if p == 'X':
                    continue
                if board[i + 1][j] == p and board[i][j + 1] == p and board[i + 1][j + 1] == p:
                    if check[i + 1][j] == 0:
                        check[i + 1][j] = 1
                        count += 1
                    if check[i][j + 1] == 0:
                        check[i][j + 1] = 1
                        count += 1
                    if check[i + 1][j + 1] == 0:
                        check[i + 1][j + 1] = 1
                        count += 1
                    if check[i][j] == 0:
                        check[i][j] = 1
                        count += 1

        q = collections.deque()
        for j in range(n):
            for i in range(m - 1, -1, -1):
                if check[i][j] == 0:
                    q.append(board[i][j])
            for i in range(m - 1, -1, -1):
                if q:
                    board[i][j] = q.popleft()
                else:
                    board[i][j] = 'X'

        answer += count
    return answer