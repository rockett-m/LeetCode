class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(n+1):
            if (i == 0):
                pass
            elif (i % 3 == 0) and (i % 5 == 0):
                output.append('FizzBuzz')
            elif (i % 3 == 0):
                output.append('Fizz')
            elif (i % 5 == 0):
                output.append('Buzz')
            else:
                output.append(str(i))
        return output