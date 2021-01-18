class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = dict()
        # 문장에서 !?,'.; 를 빼고 ' '(space)로 치환한다. 그 후 split()을 한 단어 리스트에서 단어가 banned가 아닌것만으로 리스트를 만든다.
        words = [word for word in re.sub(r'[!?,\'.;]', ' ', paragraph).lower().split() if word not in banned]
        for word in words:
            if not dic.get(word):
                dic[word] = 1
            else:
                dic[word] += 1
        # value로 딕셔너리 소팅하기!! => 일단 소팅할 인자값으로는 dic.items()를 넣어주고 key값으론 value를 넣어준다( lambda x : x[1] )
        # 오름차순 정렬을 위해 reverse=True 추가
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return dic[0][0]
