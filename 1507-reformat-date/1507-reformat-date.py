import re
class Solution:
    def reformatDate(self, date: str) -> str:
        
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        fields = date.split(' ')
        month = fields[1]
        day = str(date[0:2])
        
        int_count=0
        for i in range(len(day)):
            result = re.search(r"([A-Za-z])",day[i])
            if not result:
                int_count+=1
        if int_count == 1:
            day = "0" + day[0]
        
        count = 1
        for x in months:
            if x == month:
                if len(str(count)) < 2:
                    mon = "0" + str(count)
                else:
                    mon = str(count)
                break
            count += 1
        
        return date[-4:]+'-'+mon+'-'+day