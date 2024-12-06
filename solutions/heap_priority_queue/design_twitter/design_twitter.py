import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # ordered starting from recent
        min_heap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweet_id = self.tweetMap[followeeId][index]
                min_heap.append([count, tweet_id, followeeId, index - 1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweet_id, followeeId, index = heapq.heappop(min_heap)
            res.append(tweet_id)

            if index >= 0:
                count, tweet_id = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, [count, tweet_id, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    print("first assertion passed")
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    print("second assertion passed")
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
    print("third assertion passed")
