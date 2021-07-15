# Brute Force 풀이 O(n^2) 만큼의 시간이 소요되어 시간초과가 발생함..
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1 = words[i] + words[j]
                w2 = words[j] + words[i]
                if w1 == w1[::-1]:
                    result.append([i, j])
                if w2 == w2[::-1]:
                    result.append([j, i])

        return result


# O(k^2n)의 속도
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):  # 현재 남아있는 일부 단어가 팰린드롬인가?
                node.palindrome_word_ids.append(index)
            node = node.children[char]  # 다음 단어 일부분 검사
        node.word_id = index  # 단어의 끝지점 노드엔 index를 표시해둠

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return results




