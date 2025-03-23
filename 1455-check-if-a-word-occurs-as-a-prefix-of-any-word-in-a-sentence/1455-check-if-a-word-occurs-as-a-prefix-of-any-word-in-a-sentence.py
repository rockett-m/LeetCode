class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for idx, word in enumerate(words):
            if len(searchWord) > len(word):
                continue
            if word[0:len(searchWord)] == searchWord:
                return idx + 1

        return -1