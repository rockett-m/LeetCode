class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        ans = []

        for idx, word in enumerate(words):
            suffix = 'a' * (idx+1)

            if word[0].lower() in "aeiou":
                word += "ma"
            else:
                word += word[0] + "ma"
                word = word[1:]

            word += suffix
            ans.append(word)

        return ' '.join(ans)
