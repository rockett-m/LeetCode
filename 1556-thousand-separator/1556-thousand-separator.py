class Solution:
    def thousandSeparator(self, n: int) -> str:

        word = str(n)
        if len(str(n)) < 4:
            return word

        temp = []
        for i in range(len(word)):
            temp.append(word[i])
            if (((len(word) - i) % 3) == 1) and ((len(word)-i) > 3):
                temp.append('.')
        return ''.join(temp)