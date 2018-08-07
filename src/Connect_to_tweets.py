#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
  
import time


class myListener(StreamListener): # creating a streaming
    count = 0
    # class which writes data to a json file
    def on_status(self, status):
        
        try:
            #print status.text.encode('utf_8')
            self.count = self.count + 1
            print self.count
            #print type(data.encode('utf_8'))
            savefile = open('twitterData06.json', 'a')
            savefile.write(status.text.encode('utf_8'))           
            savefile.close()          
           
            return True #to continue listening as new events happen\n",
         
        except BaseException, e:
            print 'Failed on Data', str(e)
            time.sleep(5)
    
    def on_error(self, status): 
        print (status)



