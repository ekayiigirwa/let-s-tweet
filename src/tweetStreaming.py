#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
  
import time
from Connect_to_tweets import myListener, StreamListener


#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
if __name__ == '__main__':     
    
    #create Mylistener object \n",
    listener =myListener()
    auth = OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)
        
    #create a stream session object with the two of its parameters; auth and listener\n",
    stream = Stream(auth, listener) 
    
    # the user provides a word to track in tweets in order to count how many time it is tweeted about\n",
        
    entered_word = 'rwanda'
    
    #This line filter Twitter Streams to capture data by the keywords: 'Rwanda'\n",
    stream.filter(track=[entered_word.lower(), entered_word.upper()])
