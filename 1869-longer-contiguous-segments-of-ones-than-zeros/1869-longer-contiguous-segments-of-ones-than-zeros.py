class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros = [0]
        ones = [0]
        
        curr = -1
        count = 0

        for i in range(len(s)):

            if i == 0:
                count += 1

                if int(s[i]) % 2 == 0:
                    zeros.append(count)
                else:
                    ones.append(count)

            else:

                if int(s[i]) % 2 == 0:

                    if curr == s[i]:
                        count += 1
                    else:
                        count = 1
                    zeros.append(count)
                        
                else:

                    if curr == s[i]:
                        count += 1
                    else:
                        count = 1
                    ones.append(count)
        
            curr = s[i]

        print(ones, zeros)
        print(max(zeros))
        if max(ones) > max(zeros):
            return True
        
        return False