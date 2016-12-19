# Created by: Rory Williams Doyle
# Created on: 18/12/2016
# Last modified: 18/12/2016
# Version: 2.0

import twitter
import threading
from queue import Queue
import random
import time
import uuid


class Bot(object):
    def __init__(self):
        f = open("Keys.txt", "r")
        temp = f.readlines()
        f.close()
        keys = []
        # Strips newline characters from the read in keys.
        for key in temp:
            keys.append(key.rstrip())
        c_key = keys[0]
        c_secret = keys[1]
        t_key = keys[2]
        t_secret = keys[3]
        # Sets up the api for use.
        self.api = twitter.Api(consumer_key=c_key,
                               consumer_secret=c_secret,
                               access_token_key=t_key,
                               access_token_secret=t_secret)

Gleeson = Bot()
queue = Queue()
Gleeson_lock = threading.Lock()


def tweet(worker):
    f = open("Tweets.txt", "r")
    temp = f.readlines()
    f.close()
    tweets = []
    for line in temp:
        tweets.append(line.rstrip())
    while True:
        number = random.randrange(0, len(temp))
        error = 0
        while error == 0:
            try:
                with Gleeson_lock:
                    Gleeson.api.PostUpdates(tweets[number])
                    print("Tweeted.")
                    error = 1
            except twitter.error.TwitterError:
                print("Tweet Failed.")
        time.sleep(1800)


def re_tweet(worker):
    try:
        with Gleeson_lock:
            number = uuid.uuid1().int >> 64
            Gleeson.api.PostRetweet(number)
            print("Re-Tweeted.")
    except:
        print("Re-Tweet Failed.")


def threader():
    while True:
        worker = queue.get()
        tweet(worker)
        re_tweet(worker)
        queue.task_done()

# This for loop defines the number of threads(workers) available to the programme to work with
for x in range(2):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

for worker in range(1):
    queue.put(worker)

queue.join()
