class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        out = ''
        for i in range(len(s)):
            if s[i] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                vowels.append(s[i])
        # vowels = vowels[::-1] # reverse
        for i in range(len(s)):
            if s[i] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                out += vowels.pop(-1)
            else:
                out += s[i]
        return out