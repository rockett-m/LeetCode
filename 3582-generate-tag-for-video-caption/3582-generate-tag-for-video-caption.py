class Solution:
    def generateTag(self, caption: str) -> str:
        strs = caption.strip()
        strs = strs.split(' ')

        ans = "#"

        for i in range(len(strs)):

            if strs[i] != " ":
                if i == 0:
                    ans += strs[0].lower()
                else:  
                    ans += strs[i].capitalize()

        # ans += "".join(strs)
        return ans[:100]