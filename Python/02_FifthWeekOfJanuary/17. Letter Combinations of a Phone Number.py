# My Solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 순서 노상관 조합
        def dfs(index):
            if len(tmp) == len(digits):
                output.append(''.join(tmp))
                return
            for i in range(index, len(digits)):
                for alpha in alphas[i]:
                    tmp.append(alpha)
                    dfs(i + 1)
                    tmp.pop()

        if not digits:
            return []

        # 딕셔너리로 자판에 대한 알파벳 저장 (변환용)
        dic = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        output = []
        result = []
        digits = list(map(int, digits))
        alphas = []
        tmp = []
        for digit in digits:
            alphas.append(dic[digit])

        dfs(0)
        return output

# Book Solution
class Solution:
    # 좀 더 깔끔하게 짤 수 있지만 속도는 비슷하다.
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)  # i는 조합을 위해 문자가 중복되지 않게 선택할 수 있게 해줌.
                    # path + j로 넘겼기에 pop이나 join을 해줄 필요가 없다는 장점이있다.

        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        dfs(0, "")
        return result