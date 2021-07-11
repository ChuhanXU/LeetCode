# python list 直接加中括号就行了
# for key,value in hash 要用hash.items()不然会出现object not iterate error

# 1.postTweet(userId,tweetId)
# check if the user is other's follower
# postTweet(1,5)

# userIdPost[userId].append(tweetId)
# for item in followerfee[userId]:
# userIdPost[item].append(tweetId)

# 2.getNewsFeed(uersId)
# return list(reversed(userIdPost[usersId]))[:10]

# 3.follow(followerId,followeeId)
# follow(1,2)
# follow(1,3)
# followerfee={1:[2,3]}

# 4.unfollow(followerId,followeeId)
# unfollow(1,2)
# followerfee[followerId].remove(followeeId)

# 1.what data types of these all ID, they are all int right?
import collections


class Twitter(object):
#     then I need to initialize my data structure
    def __init__(self):
        self.userIdPost={}
        self.followerfee={}
    def postTweet(self, userId, tweetId):
        if userId not in self.userIdPost.keys():
            self.userIdPost[userId]=[tweetId]
        else:
            self.userIdPost[userId].append(tweetId)
        #     check if this user is others followers
        for key,value in self.followerfee.items():
            if userId in value:
                fee = key
                self.userIdPost[fee].append(tweetId)

        return self.userIdPost

    def getNewsFeed(self,userId):
        return list(reversed(self.userIdPost[userId]))[:10]

    def follow(self,followerId,followeeId):
        if followeeId not in self.followerfee.keys():
            self.followerfee[followeeId]=[followerId]
        else:
            self.followerfee[followeeId].append(followerId)
        return self.followerfee

    def unfollow(self,followerId,followeeId):
        if followeeId in self.followerfee.keys():
            self.followerfee[followeeId].remove(followerId)
        #     check
        for item in self.userIdPost[followerId]:
            if item in self.userIdPost[followeeId]:
                self.userIdPost[followeeId].remove(item)



        return self.followerfee


solution=Twitter()
print(solution.postTweet(1,5))
print(solution.getNewsFeed(1))
print(solution.follow(1,2))
print(solution.postTweet(2,6))
print(solution.getNewsFeed(1))
print(solution.unfollow(1,2))
print(solution.getNewsFeed(1))



# ab={1:[1,2],2:[3,4]}
# print(ab.values())
# for key,value in ab.items():
#     print(key,value)
