class Solution:
    def mySqrt(self, x: int) -> int:    

        my_ans = -1

        for num in range(2**31):
            ans = num * num

            if ans > x:
                return my_ans

            elif ans == x:
                return num

            my_ans = num

        return my_ans
    
#     0110 -> 0010
#     4 -> 2
    
#     8 -> 2.8 -> 2
#     1000 -> 0010

#     21 -> 4.6 -> 4
#     10101 -> 0100

#     37 -> 6.1 -> 6