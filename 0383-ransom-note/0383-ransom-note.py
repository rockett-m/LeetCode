class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = list(magazine)
        for let in range(len(ransomNote)):
            if ransomNote[let] in mag_list:
                idx = mag_list.index(ransomNote[let])
                mag_list.pop(idx)
            else:
                return False
        return True