class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for idx, key in enumerate(words):
            for ix, w in enumerate(words):
                if ix > idx and w[::-1] == key:
                    count += 1

        return count