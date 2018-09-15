# coding: utf-8

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


# consumer key, consumer secret, access token, access secret.
# to keep the personal information information confidentially, I delete the following 4 lines of information
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessSecret = ""

class listener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            saveTweet = open('outputTweet.json' , 'a' , encoding = 'UTF-8' , newline = '')
            saveTweet.write(data)
            saveTweet.close()
            return(True)
        except (BaseException , error):
            print('failed streaming data' , str(error))
            

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumerKey , consumerSecret)
auth.set_access_token(accessToken , accessSecret)

inputWord = input('Please input the word you want to track: ')

def getCurrentTweet(TrackWord):
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[TrackWord])

getCurrentTweet(inputWord)