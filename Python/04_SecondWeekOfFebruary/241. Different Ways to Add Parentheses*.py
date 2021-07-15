class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        # 숫자만 있는 경우
        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            # 연산자는 분할의 기준
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                # 분할한 문제들을 정복한 값이 계속해서 compute함수로 들어감
                # append가 아닌 extend를 통해 여러값을 리스트에 같이 넣을 수 잇음
                # append와 extend의 차이
                results.extend(compute(left, right, value))

        return results