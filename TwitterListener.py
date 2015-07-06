from tweepy import OAuthHandler
from tweepy import Stream
from TwitterStreamer import TwitterStreamer

import threading

class TwitterListener:
    consumer_key="yoPKCHwC71pgLyhoNnrgpeV7f"
    consumer_secret="BSoRXjgfxEgHdFhseGFDcFqK69r9cjaxi6f3ATxrjH7HKzmfAR"
    access_token="2192556798-WgcCDSQDb0CtenSOu7hBQKDKKwhvNZiSkoig0Q1"
    access_token_secret="CNcdi0k1HKFQcamcCg57SF6fq0cbPgK4wRIlIX2Ue1VPq"
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    def __init__(self, queue):
         self.queue = queue
         self.threads = []

    def listen(self, tags):
         thread = threading.Thread(target=self.__listen_as_thread, args=(tags))
         thread.daemon = True
         self.threads.append(thread)
         thread.start()

    def __listen_as_thread(self, tags):
         listener = TwitterStreamer(self.queue)
         stream = Stream(TwitterListener.auth, listener)
         stream.filter(track=tags)
    

    
