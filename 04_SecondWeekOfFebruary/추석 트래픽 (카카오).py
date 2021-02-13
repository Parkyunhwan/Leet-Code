from datetime import datetime, timedelta
def compare(time, moment):
    start = time
    end = time + timedelta(milliseconds=999)

    if start >= moment[0] and start <= moment[1]:
        return True
    elif end >= moment[0] and end <= moment[1]:
        return True
    elif start <= moment[0] and end >= moment[1]:
        return True
    # 경우의 수 세가지
    # 1. 기준점의 start가 가운데 있는 경우 m0 s m1
    # 2. 기준점의 end가 가운데 있는 경우 m0 e m2
    # 3. 기준점의 start, end 가운데 있는 경우 s m0, m1 e
    # 4. m0 s, e m1의 경우는 1 또는 2의 경우에 포함되는 경우이다.

# 핵심
# * 문자열을 datetime과 초로 어떻게 나눌 것인가
# * 나눈 초를 어떻게 뺄것인가
# * 어떻게 1초안에 수행되는 모든 로그를 검사할 것인가
# 이 3가지에 대해 고민해보자
def solution(lines):
    result = []
    for line in lines:
        temp = line.split(' ')
        date = str(temp[0] + " " + temp[1])

        if '.' in temp[2]:
            delay = temp[2].split('.')
            delay[1] = delay[1][0:-1]  # s 삭제
        else:  # 소숫점이 없을 때
            delay = list(temp[2][0:-1])
            delay += ["0"]

        end = datetime.fromisoformat(date)

        start = end - timedelta(seconds=int(delay[0]), milliseconds=int(delay[1]) - 1)
        result.append([start, end])  # 모든 수행의 시작과 끝을 기록해둠
    print("result {}", result)
    answers = []
    for timelist in result:
        # timelist안에는 각 로그의 시작과 끝 값이 들어있음
        for time in timelist:
            # 시작과 끝 시간을 각각 검사 기준점으로 잡음
            answer = 0
            for moment in result:
                # 검사 기준점 시간으로 1초 후 시간안에 현재로그가 포함되는 검사
                # 현재 로그가 기준점에서 1초내에 포함된다면 갯수 1증가
                if compare(time, moment):
                    answer += 1
            # 포문이 종료되면 현재 기준점에 대해 모든 로그를 검사한 것임. 이 때 answer값을 기준점(time)을 기준으로 1초가 요청의 최대 개수가 됨

            # 최대 개수를 answers에 삽입
            answers.append(answer)
    return max(answers)