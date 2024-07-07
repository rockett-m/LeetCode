class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        if len(digits) < 1: return combos

        mapping = {}
        mapping['2'] = ['a', 'b', 'c']
        mapping['3'] = ['d', 'e', 'f']
        mapping['4'] = ['g', 'h', 'i']
        mapping['5'] = ['j', 'k', 'l']
        mapping['6'] = ['m', 'n', 'o']
        mapping['7'] = ['p', 'q', 'r', 's']
        mapping['8'] = ['t', 'u', 'v']
        mapping['9'] = ['w', 'x', 'y', 'z']
        
        if len(digits) == 1: return mapping[digits]

        def backtrack(idx: int, string: str):

            if idx >= len(digits):
                combos.append(string)
                return 

            for letter in mapping[digits[idx]]:
                backtrack(idx+1, f'{string}{letter}')                
            
        backtrack(0, '')
        
        return combos