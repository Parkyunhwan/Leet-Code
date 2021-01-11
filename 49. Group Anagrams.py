# 에너그램은 단어를 소팅하면 같은 단어가 된다.
# 10 -> defaultdict(list)를 사용하면 value를 list type으로 기본설정할 수 있다. int로 하면 0이 기본 설정된다.
# 12 -> 애너그램을 키 값으로 하고 각 단어를 리스트의 원소로 삽입한다. 키로 value를 조회하면 리스트가 나옴을 알수 있다.
# 13 -> .value()로 반환 시 리스트를 둘러싼 이차원 리스트가 반환된다.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()





# Wrong
# time out..
class Solution:
    def check_char(self, str1: str, str2: str) -> bool:
        ch = [0] * 26
        diff = ord('A') - ord('a')
        for c in str1:
            ch[ord(c) - ord('a')] += 1
        for c in str2:
            ch[ord(c) - ord('a')] -= 1
        for c in ch:
            if c != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = [False] * len(strs)
        ret = []
        for i in range(len(strs)):
            if check[i]:
                continue
            str = strs[i]
            temp = [str]
            check[i] = True
            for j in range(i + 1, len(strs)):
                if self.check_char(str, strs[j]) and not check[j]:
                    temp.append(strs[j])
                    check[j] = True
            ret.append(temp)
        return (ret)