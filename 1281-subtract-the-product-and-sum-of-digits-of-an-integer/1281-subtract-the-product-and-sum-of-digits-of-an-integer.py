class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = []; prod = 0; summ = 0

        if n < (pow(10, 1)):
            # return 0
            a.append(n % (pow(10, 1)))

        elif n < (pow(10, 2)):
            a.append(n % (pow(10, 1)))
            a.append(int(((n - a[0]) / (pow(10, 1))) % 10))

        elif n < (pow(10, 3)):
            a.append(n % (pow(10, 1)))
            a.append(int(((n - a[0]) / (pow(10, 1))) % 10))
            a.append(int(((n - 10*a[1] - a[0]) / (pow(10, 2)) % 10)))
            
        elif n < (pow(10, 4)):
            a.append(n % (pow(10, 1)))
            a.append(int(((n - a[0]) / (pow(10, 1))) % 10))
            a.append(int(((n - 10*a[1] - a[0]) / (pow(10, 2)) % 10)))
            a.append(int(((n - 100*a[2] - 10*a[1] - a[0]) / (pow(10, 3)) % 10)))

        elif n < (pow(10, 5)):
            a.append(n % (pow(10, 1)))
            a.append(int(((n - a[0]) / (pow(10, 1))) % 10))
            a.append(int(((n - 10*a[1] - a[0]) / (pow(10, 2)) % 10)))
            a.append(int(((n - 100*a[2] - 10*a[1] - a[0]) / (pow(10, 3)) % 10)))
            a.append(int(((n - 1000*a[3] - 100*a[2] - 10*a[1] - a[0]) / (pow(10, 4)) % 10)))
            
        for i in range(len(a)):
            # print(i, a[i])
            if i == 0:
                prod = a[i]; summ = a[i]
            else:
                prod = a[i] * prod
                summ = a[i] + summ

        return prod - summ
