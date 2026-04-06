class Twitter(object):
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []
        if userId not in self.following:
            self.following[userId] = {userId}

        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId):
        all_relevant_tweets = []
        friends = self.following.get(userId, {userId})
        friends.add(userId) 
        
        for f_id in friends:
            if f_id in self.tweets:
                all_relevant_tweets.extend(self.tweets[f_id][-10:])
                all_relevant_tweets.sort(key=lambda x: x[0], reverse=True)
        
        result = []
        for i in range(min(10, len(all_relevant_tweets))):
            result.append(all_relevant_tweets[i][1])
            
        return result
        

    def follow(self, followerId, followeeId):
        if followerId not in self.following:
            self.following[followerId] = {followerId}
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following and followeeId != followerId:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
              
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
