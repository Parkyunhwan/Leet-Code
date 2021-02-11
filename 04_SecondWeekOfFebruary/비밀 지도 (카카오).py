def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    for i in range(len(arr1)):
        c = arr1[i] | arr2[i]
        c = bin(c)[2:]
        while len(c) != len(arr1):
            c = '0' + c
        c = c.replace('0', ' ')
        c = c.replace('1', '#')

        answer.append(c)
    return answer

# rjust로 간단하게 원하는문자를 채울 수도 있따.
# https://kkamikoon.tistory.com/136
# 25분