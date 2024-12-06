from typing import List


class Twitter:

    def __init__(self):
        return

    def postTweet(self, userId: int, tweetId: int) -> None:
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        return []

    def follow(self, followerId: int, followeeId: int) -> None:
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        return


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
