def solution(dartResult):
    dartList = []
    tmp = []
    resultList = []
    answer = 0
    for dr in dartResult:
        if dr.isdigit():
            if tmp and tmp[-1].isdigit():
                tmp[-1] = tmp[-1] + dr
                continue
            if tmp and not tmp[-1].isdigit():
                dartList.append(tmp)
                tmp = []
            tmp.append(dr)
        else:
            tmp.append(dr)
    if tmp:
        dartList.append(tmp)
    print(dartList)
    for i, val in enumerate(dartList):
        score = int(val[0])
        bonus = val[1]
        if bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3

        if len(val) == 3:
            option = val[2]
            if option == '*':
                if i > 0:
                    resultList[i - 1] *= 2
                score *= 2
            elif option == '#':
                score *= -1
        resultList.append(score)
    answer = sum(resultList)
    return answer