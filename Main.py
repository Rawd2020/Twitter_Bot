# Created by: Rory Williams Doyle
# Created on: 18/12/2016
# Last modified: 21/12/2016
# Version: 2.2

# These import statements import all the external libraries used in the bot.
import twitter
import threading
from queue import Queue
import random
import time


# This function is designed to remove the repeated code for
# reading in files and removing new line characters.
def read_in(file_name, permission):
    file = open(file_name, permission)
    temporary = file.readlines()
    file.close()
    data = []
    for item in temporary:
        data.append(item.rstrip())
    return data
# Reading in keys from text file.
keys = read_in("Keys.txt", "r")
c_key = keys[0]
c_secret = keys[1]
t_key = keys[2]
t_secret = keys[3]
# Sets up the api for use.
api = twitter.Api(consumer_key=c_key,
                  consumer_secret=c_secret,
                  access_token_key=t_key,
                  access_token_secret=t_secret)
# Reading in hashtags from text file.
hashtags = read_in("Hashtags.txt", "r")
# Reading in tweets from text file.
tweets = read_in("Tweets.txt", "r")
# Creates the job queue.
queue = Queue()


# This job is for sending out random pre-written tweets periodically.
def tweet(worker_thread):
    # This number is used to pick a random tweet.
    number = random.randrange(0, len(tweets))
    # Tries to post tweet but built in exception in case the tweet fails.
    post = 0
    while post == 0:
        try:
            api.PostUpdates(tweets[number])
            print("Tweeted.")
            post = 1
        except twitter.error.TwitterError:
            print("Tweet Failed.")


# This job is for re-tweeting tweets periodically.
def re_tweet(worker_thread):
    # Tries to make a re-tweet but has a built in exception in case it fails.
    post = 0
    while post == 0:
        try:
            # This number is used to pick a random hashtag for the search.
            number = random.randrange(0, len(hashtags))
            hashtag = hashtags[number]
            # Searched for a tweet using a random hashtag and posts the first result.
            api.PostRetweet(api.GetSearch(
                raw_query="q=%23"+hashtag+" lang%3Aen&count=1")[0].id_str)
            print("Re-Tweeted.")
            post = 1
        except twitter.error.TwitterError:
            print("Re-Tweet Failed.")


# The threader handles the distribution of jobs to the threads(workers).
def threader():
    # Main programme loop.
    while True:
        worker_thread = queue.get()
        number = random.randint(0, 1)
        # The worker is assigned a random job based off the randomly generated number variable.
        if number == 0:
            tweet(worker_thread)
            queue.task_done()
        elif number == 1:
            re_tweet(worker_thread)
            queue.task_done()
        else:
            print("Threader number error.")
            break
        # This wait period defines the gap between when the bot finishes a job and when it moves onto the next.
        time.sleep(1800)

# This for loop defines the number of threads(workers) available to the programme to work with
for x in range(1):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

# This loop defines the number of jobs in the queue.
for worker in range(1000):
    queue.put(worker)

# Starts the main thread.
queue.join()
