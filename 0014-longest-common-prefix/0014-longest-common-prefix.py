import numpy as np

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        char = ''; common = ''

        for i in range(0, len(min(strs))):
            for string in strs:
                
                if char == '': char = string[i]
                    
                elif char != string[i]: return common

            common = common + char; char = ''

        return common
