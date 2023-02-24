class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = str(bin(n))[2:]
        count = 0
        for i in range(len(bin_n)):
            if int(bin_n[i]) == 1:
                count += 1
        return count
            # print(i, bin_n[i])
#         print(bin(n))
#         count = 0
#         while n > 1:
#             print('start,', n)
#             n = n // 2
#             count += 1
#             print(n, count)
#         print(count)
#         return count
# #         n_s = str(n)
# #         print(n_s, len(n_s))
#         count = 0
#         for digit in range(len(n_s)):
#             # print(digit, count)
#             if int(n_s[digit]) == 1:
#                 count += 1
#             print(digit, count)

#         return count
#         # print([char == 1 for char in range(len(str(n)))])
#         # return sum([char == 1 for char in range(len(str(n)))])
