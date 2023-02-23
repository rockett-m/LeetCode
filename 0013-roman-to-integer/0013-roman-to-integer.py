class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = { 'I' : 1,
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000 }

        total = 0; prev = ''

        for i in range(len(s)):
            curr = s[i]

            if len(s) == 0: return total

            elif len(s) == 1: return my_dict[curr]

            else: # len >= 2
                # if special char, then don't add it, go to check next char
                if (curr in ['V', 'X'] and prev == 'I') or (curr in ['L', 'C'] and prev == 'X') or (curr in ['D', 'M'] and prev == 'C'):
                    total += (my_dict[curr] - my_dict[prev]) # special case subtraction
                    prev = ''
                    if (len(s) - 1 == i): return total

                else:
                    if prev != '':
                        total += my_dict[prev]
                    prev = curr

        return total + my_dict[curr]
