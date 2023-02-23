class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        
        prev = ''
        for i in command:
            if i == "G":
                output = output + i
            elif i == "(":
                prev = i
            elif (i == ")") and (prev == "("):
                output = output + "o"
                prev = ''
            elif i == "a":
                prev = prev + i
            elif i == "l":
                prev = prev + i
            elif i == ")" and (prev == "(al"):
                output = output + "al"
                prev = ''
        
        return output