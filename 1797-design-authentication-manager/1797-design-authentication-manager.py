class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        # add currentTime + timeToLive
        if tokenId in self.tokens.keys() and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        if not self.tokens: return 0
        return sum(1 for v in self.tokens.values() if v > currentTime)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)