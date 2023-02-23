class Solution:
    def mySqrt(self, x: int) -> int:    

        my_list = [-1, -1]

        for num in range(2**31):
            ans = num * num
            if ans == x:
                return num
            elif ans > x:
                return my_list[0]
            
            my_list = [num]

        return my_list[0]
    
#     0110 -> 0010
#     4 -> 2
    
#     8 -> 2.8 -> 2
#     1000 -> 0010

#     21 -> 4.6 -> 4
#     10101 -> 0100

#     37 -> 6.1 -> 6