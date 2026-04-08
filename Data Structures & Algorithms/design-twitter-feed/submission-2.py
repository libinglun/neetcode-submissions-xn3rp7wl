import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user2tweet = defaultdict(list)
        self.user2follow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user2tweet[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        limit = 10

        followed = self.user2follow[userId]
        followed.add(userId)
        
        # Merge all the tweets by user itself and its followed users
        all_tweets = []
        for user in followed:
            all_tweets.extend(self.user2tweet[user])
        heapq.heapify_max(all_tweets)

        result = []
        while all_tweets and limit:
            result.append(heapq.heappop_max(all_tweets)[1])
            limit -= 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user2follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user2follow[followerId]:
            self.user2follow[followerId].remove(followeeId)
        
