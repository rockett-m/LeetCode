class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        fields = text.split(' ')
        count = len(fields)

        for w in fields:
            for l in brokenLetters:
                if l in w:
                    count -= 1
                    break

        return count
            