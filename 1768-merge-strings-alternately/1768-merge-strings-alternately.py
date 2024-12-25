class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        common = min(len(word1), len(word2))
        output = ''
        for i in range(common):
            output += word1[i] + word2[i]
        if len(word1) > len(word2):
            output += word1[common:]
        elif len(word2) > len(word1):
            output += word2[common:]
            
        return output
