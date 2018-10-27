import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from HTMLParser import HTMLParser

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = "ta4iDC8at7SaXxSyvHH4e1aok"
consumer_secret = "ACZTXH22tOz0dWwwe2mzdYj4DdjzGVsJtdtkR4d37q8Mw4Sg0s"
access_token = "72847913-YiJi0970duy6LHzApaOanN6A6I8S2KG28Du4tx0QH"
access_token_secret= "6N0kabWQTclJCT1aAtTdJup8VYrKZZf5vwvlLyCVFvwlN"

# This is the listener, resposible for receiving data
class StdOutListener(StreamListener):
    def on_data(self, data):
        # Parsing
        decoded = json.loads(data)
        #open a file to store the status objects
        file = open('stream.json', 'a')
        #write json to file
        json.dump(decoded,file,sort_keys = True,indent = 4)

        #show progress
        print("Writing tweets to file,CTRL+C to terminate the program")


        return True



    def on_status(self, status):

		#print "\n Text\n",status.text,"\n\nGEO\n\n"

		if status.coordinates:
            		print 'coords:', status.coordinates

        	if status.place:
            		print 'place:', status.place.full_name

        	return True


    def on_error(self, status):
        print(status)
        if status ==420:
            return False
        sys.exit()

#if __name__ == '__main__':

def main():
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

        # There are different kinds of streams: public stream, user stream, multi-user streams
        # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)

    #working login to fetch tweet
    #can be changed to the hurricane or earthquake hastag
    
    stream.filter(track=["#MeToo"])

if __name__ == '__main__':
    main()
