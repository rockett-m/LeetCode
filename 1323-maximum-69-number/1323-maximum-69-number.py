class Solution:
    def maximum69Number (self, num: int) -> int:

        my_li = list(str(num))
        
        for elem in range(len(my_li)):
            if my_li[elem] == "6":
                my_li[elem] = "9"
                break
                
        return int(''.join(my_li))