class Twitter:

    def __init__(self):
        self.followers = OrderedDict()
        self.tweets = []
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets.append((-self.count, tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweets.copy()
        heapify(tweets)
        recent = []
        # min heap
        while tweets and len(recent) < 10:
            count, tweetId, user = heappop(tweets)
            if user == userId:
                recent.append(tweetId)
            elif (userId) in self.followers.keys() and \
                user in self.followers[(userId)]:
                recent.append(tweetId)

        return recent

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers.keys():
            self.followers[(followerId)] = set()
        self.followers[(followerId)].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId) not in self.followers.keys():
            return
        if followeeId in self.followers[(followerId)]:
            self.followers[(followerId)].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)