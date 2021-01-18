class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit

# lambdat 사용하는 법, key 사용법, 리스트 컴프리헨션 사용법