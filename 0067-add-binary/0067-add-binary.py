class Solution:
    def addBinary(self, a: str, b: str) -> str:

        la, lb = len(a), len(b)
        diff = abs(la-lb)
        if la < lb:    a = '0'*diff + a
        elif la > lb:  b = '0'*diff + b

        c = False
        ptr = len(a)-1
        ans = ''
    
        while ptr >= 0:

            new = '0'
            ai, bi = int(a[ptr]), int(b[ptr])
            if ai + bi == 2:
                if c: new = '1'
                c = True

            elif ai + bi == 1:
                if not c: new = '1'
                else: c = True

            else:
                if c: new = '1'
                c = False

            ans = f'{new}{ans}'
            ptr -= 1

        return f'1{ans}' if c else ans
