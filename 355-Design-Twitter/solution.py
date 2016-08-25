class Twitter(object):

    MAX_TWEETS = 10
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        #self.user_tweets = collections.defaultdict(collections.deque)
        self.user_tweets = {}
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.user_tweets:
            self.user_tweets[userId] = collections.deque(maxlen=Twitter.MAX_TWEETS)
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        sorted_tweets = list()
        people = self.followers.get(userId, set()) | set([userId])

        for f in people:
            if f in self.user_tweets:
                for tweets in self.user_tweets[f]:
                    sorted_tweets.append(tweets)
        heapq.heapify(sorted_tweets)
        res = []
        while len(res) < 10 and sorted_tweets:
            res.append(heapq.heappop(sorted_tweets)[1])
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)