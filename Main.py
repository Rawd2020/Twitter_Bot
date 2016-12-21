# Created by: Rory Williams Doyle
# Created on: 18/12/2016
# Last modified: 21/12/2016
# Version: 3.1

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


# Reading in bot settings from Config.txt
SETTINGS = read_in("Config.txt", "r")
# Sets up the api for use using the keys from Config.txt.
api = twitter.Api(consumer_key=SETTINGS[0].split("=")[1],
                  consumer_secret=SETTINGS[1].split("=")[1],
                  access_token_key=SETTINGS[2].split("=")[1],
                  access_token_secret=SETTINGS[3].split("=")[1])
# Reading in hashtags from text file.
hashtags = read_in("Hashtags.txt", "r")
# Reading in tweets from text file.
tweets = read_in("Tweets.txt", "r")
# Creates the job queue.
queue = Queue()
# A simple thread lock to prevent data corruption.
twitter_lock = threading.Lock()


# This job is for sending out random pre-written tweets periodically.
def tweet(worker_thread):
    # This loop handles the picking of a valid tweet from Tweets.txt to post.
    # It will inform the user if any tweet is over the 140 character limit.
    while True:
        number = random.randrange(0, len(tweets))
        if len(tweets[number]) <= 140:
            break
        else:
            print("This tweet is over the character limit: "+tweets[number])
    # Tries to post tweet but built in exception in case the tweet fails.
    while True:
        try:
            with twitter_lock:
                api.PostUpdates(tweets[number])
                print("Tweeted.")
                break
        except twitter.error.TwitterError:
            with twitter_lock:
                print("Tweet Failed.")


# This job is for re-tweeting tweets periodically.
def re_tweet(worker_thread):
    # Tries to make a re-tweet but has a built in exception in case it fails.
    while True:
        try:
            with twitter_lock:
                # This number is used to pick a random hashtag for the search.
                number = random.randrange(0, len(hashtags))
                hashtag = hashtags[number]
                try:
                    # Searched for a tweet using a random hashtag and posts the first result.
                    api.PostRetweet(api.GetSearch(raw_query="q=%23"+hashtag+" lang%3Aen&count=1")[0].id_str)
                    print("Re-Tweeted.")
                    break
                except IndexError:
                    print("This hashtag is not returning any object: "+hashtag)
        except twitter.error.TwitterError:
            with twitter_lock:
                print("Re-Tweet Failed.")


# This job makes the bot follow another twitter user.
def friend(worker_thread):
    # Tries to follow a user but has a built in exception in case it fails.
    while True:
        try:
            with twitter_lock:
                number = random.randrange(0, len(hashtags))
                hashtag = hashtags[number]
                try:
                    result = api.GetSearch(raw_query="q=%23" +hashtag + " lang%3Aen&count=1")[0].user
                    api.CreateFriendship(result.id)
                    print("Following: "+result.screen_name)
                    break
                except IndexError:
                    print("This hashtag is not returning any object: "+hashtag)
        except twitter.error.TwitterError:
            with twitter_lock:
                print("Follow Failed")


# The threader handles the distribution of jobs to the threads(workers).
def threader():
    # Main programme loop.
    if (SETTINGS[7].split("=")[1]) == "Default":
        while True:
            worker_thread = queue.get()
            number = random.randint(0, 2)
            # The worker is assigned a random job based off the randomly generated number variable.
            if number == 0:
                tweet(worker_thread)
                queue.task_done()
            elif number == 1:
                re_tweet(worker_thread)
                queue.task_done()
            elif number == 2:
                friend(worker_thread)
                queue.task_done()
            else:
                print("Threader number error.")
                break
            # This wait period defines the gap between when the bot finishes a job and when it moves onto the next.
            time.sleep(int(SETTINGS[4].split("=")[1]))
    else:
        print("Non-Default functionality has not been programmed yet!")


# This for loop defines the number of threads(workers) available to the programme to work with
for x in range(int(SETTINGS[6].split("=")[1])):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

# This loop defines the number of jobs in the queue.
for worker in range(int(SETTINGS[5].split("=")[1])):
    queue.put(worker)

# Starts the main thread.
queue.join()
