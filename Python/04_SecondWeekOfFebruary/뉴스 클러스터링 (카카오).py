import collections


def solution(str1, str2):
    def split2str(s):
        tmp, li = [], []
        for char in s:
            if not char.isalpha():
                if tmp:
                    tmp.pop()
                continue
            if not tmp:
                tmp.append(char)
            else:
                li.append((tmp[0] + char).lower())
                tmp.pop()
                tmp.append(char)
        return li

    answer = 0
    gyo = 0
    hap = 0
    list1 = split2str(str1)
    list2 = split2str(str2)
    dic1, dic2 = collections.defaultdict(int), collections.defaultdict(int)
    for l1 in list1:
        dic1[l1] += 1
    for l2 in list2:
        dic2[l2] += 1

    ss = set(list1).union(set(list2))
    for comp in list(ss):
        val1, val2 = dic1[comp], dic2[comp]
        if val1 > 0 and val2 > 0:
            gyo += min(val1, val2)
        hap += max(val1, val2)

    if gyo == 0 and hap == 0:
        answer = 1
    else:
        answer = gyo / hap
    answer = int(answer * 65536)
    return answer