# Created by: Rory Williams Doyle
# Created on: 18/12/2016
# Last modified: 20/12/2016
# Version: 2.1

# These import statements import all the external libraries used in the bot.
import twitter
import threading
from queue import Queue
import random
import time
import uuid


# This class defines a bot and sets up the keys for OAuth with the twitter api.
class Bot(object):
    def __init__(self):
        # Reading in keys from text file.
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

# This is where you define your bot instances and set up the queue and lock for the threads. I called my bot Gleeson.
Gleeson = Bot()
queue = Queue()
Gleeson_lock = threading.Lock()


# This job is for sending out random pre-written tweets periodically.
def tweet(worker):
    # Reading in tweets from text file.
    f = open("Tweets.txt", "r")
    temp = f.readlines()
    f.close()
    tweets = []
    # Strips newline characters from the read in tweets.
    for line in temp:
        tweets.append(line.rstrip())
    # This number is used to pick a random tweet.
    number = random.randrange(0, len(temp))
    # Tries to post tweet but built in exception in case the tweet fails.
    try:
        with Gleeson_lock:
            Gleeson.api.PostUpdates(tweets[number])
            print("Tweeted.")
    except twitter.error.TwitterError:
        print("Tweet Failed.")


# This job is for re-tweeting tweets periodically.
def re_tweet(worker):
    # Tries to make a re-tweet but has a built in exception in case it fails.
    try:
        with Gleeson_lock:
            number = uuid.uuid1().int >> 64
            Gleeson.api.PostRetweet(number)
            print("Re-Tweeted.")
    except twitter.error.TwitterError:
        print("Re-Tweet Failed.")


# The threader handles the distribution of jobs to the threads(workers).
def threader():
    # Main programme loop.
    while True:
        worker = queue.get()
        number = random.randint(0,1)
        print(number)
        # The worker is assigned a random job based off the randomly generated number variable.
        if number == 0:
            tweet(worker)
            queue.task_done()
        elif number == 1:
            re_tweet(worker)
            queue.task_done()
        else:
            print("Threader number error.")
            break
        # This wait period defines the gap between when the bot finishes a job and when it moves onto the next.
        time.sleep(900)

# This for loop defines the number of threads(workers) available to the programme to work with
for x in range(1):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

# This loop defines the number of jobs in the queue.
for worker in range(5):
    queue.put(worker)

# Starts the main thread.
queue.join()
