class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        self.ans = []
        self.stack = []
        
        for x in range(1, n+1):
            self.push(x)
            if x not in target:
                self.pop()
            if target == self.stack:
                return self.ans

    def push(self, n: int):
        self.stack.append(n)
        self.ans.append('Push')
        
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.ans.append('Pop')
