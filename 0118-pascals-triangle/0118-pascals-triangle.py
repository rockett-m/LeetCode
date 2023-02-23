class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        full_list = []
        
        if numRows < 1:
            return
            
        elif numRows == 1:
            full_list.append([1])     # build row 1
            return full_list
            
        elif numRows == 2:
            full_list.append([1])     # build row 1
            full_list.append([1, 1])  # build row 2
            return full_list
        
        else:  # numRows >= 3

            for i in range(1, numRows+1):  # 1-indexed since we can't have 0 rows

                row_list = [1]*i            # populate all elems in row with 1 to start
                
                if i <= 2:
                    full_list.append(row_list)  # can directly append row 1,2 without modification

                else: # i >= 3
                    
                    prevRow = full_list[i-2]  # row2 is [1, 1]

                    for j in range(i):  # 0...currRowLen-1    (0-indexed)

                        if (j > 0) and (j < i-1):  # addition required
                            curr = prevRow[j-1] + prevRow[j]
                            row_list[j] = curr
                        
                    full_list.append(row_list)

            return full_list