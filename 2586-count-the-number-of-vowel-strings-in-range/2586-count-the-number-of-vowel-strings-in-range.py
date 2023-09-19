class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for w in words[left:right+1]:
            if w[0] in vowels and w[-1] in vowels:
                count += 1
        return count