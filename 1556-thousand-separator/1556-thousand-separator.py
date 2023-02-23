class Solution:
    def thousandSeparator(self, n: int) -> str:
        word = str(n)
        temp = ''
        if len(word) < 4:
            return word
        else:
            for i in range(len(word)):
                temp = temp + str(word[i])
                if (((len(word) - i) % 3) == 1) and ((len(word)-i) > 3):
                    temp=temp+'.'
        return temp