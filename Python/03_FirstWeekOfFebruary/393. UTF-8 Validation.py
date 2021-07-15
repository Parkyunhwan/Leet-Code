class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            # i = 1
            # while i <= size:
            #     if data[start + i] >> 6 == 0b10:
            #         i += 1
            #     else:
            #         return False
            # return True
            i = 1
            while i <= size:
                if i >= len(data):
                    return False
                if data[start + i] >> 6 == 0b10:
                    i += 1
                else:
                    return False
            return True

        start = 0

        while start < len(data):

            first = data[start]
            # 3개 밀어내고 남은 나머지 5개가 11110 인지 검사 (4byte)
            # 11110 이라면 나머지 바이트 3개가 10인지 검사
            if (first >> 3) == 0b11110 and check(3):
                start += 4  # 4바이트가 하나의 문자!
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:  # 첫 비트가 0으로 시작이면 1byte 문자 (128 개)
                start += 1
            else:
                return False
        return True