'''
시간과 관련된 문제를 푸는 방법...

* 시, 분으로 나눠져 있는 것을 분으로 환산한다.
* 조건을 작게 분할해서 해결한다.
'''
def solution(n, t, m, timetable):
    answer = ''
    # 시간과 분으로 나뉘어져있는 것을 분으로 환산한다.
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()

    # last_time은 마지막 셔틀버스가 도착하는 시간을 뜻한다.
    last_time = (60 * 9) + (n - 1) * t

    # 모든 운행횟수를 반복한다.
    for i in range(n):
        # 셔틀 총 인원 보다 남은 인원이 작다면 주인공은 여유롭게 마지막 버스 도착 시간에 맞춰가도록 한다.
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # 현재 버스가 마지막 버스라면 (이전 조건에 의해 주인공 포함 남은 인원은 모두 셔틀버스에 탈 수 없음)
        if i == n - 1:
            # 마지막 버스 도착시간 전에 사람들이 기다리고 있다면
            if timetable[0] <= last_time:
                # 셔틀 총 인원의 마지막에 탑승하는 사람보다 1분 빠른 시간을 선점한다.
                last_time = timetable[m - 1] - 1
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # 마지막 버스가 아니라면
        for j in range(m - 1, -1, -1):
            # 버스의 도착시간을 분으로 계산
            bus_arrive = (60 * 9) + i * t
            # 남아있는 대기 인원 중 버스 도착 보다 빠른 인원 탑승(삭제) - 최대 m 만큼
            if timetable[j] <= bus_arrive:
                del timetable[j]

#---
#재풀이 실패..ㅠㅠ
def convertHourToMinute(timetable):
    result = []
    for time in timetable:
        hours = int(time[:2])
        minutes = int(time[3:])
        result.append(60 * hours + minutes)
    return result


def solution(n, t, m, timetable):
    answer = ''
    timetable = convertHourToMinute(timetable)
    startTime = 60 * 9
    departTime = 60 * 9
    last = departTime
    for i in range(n):
        departTime = startTime + (i * t)
        last = departTime
        count = 0
        while timetable and departTime >= timetable[0]:
            if count == m:
                break
            last = timetable.pop(0)
            count += 1
        if i == n - 1:

            if timetable and timetable[0] == last:
                answer = last - 1
            else:
                answer = last

    hour = answer // 60
    minute = answer % 60
    answer = str(hour) + ":" + str(minute)
    return answer
