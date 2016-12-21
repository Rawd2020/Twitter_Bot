WELCOME TO TWITTER BOT! :D

Created by: Rory Williams Doyle
Created on: 18/12/2016
Last modified: 21/12/2016
Software version: 3.1
README last update: 21/12/2016

System Requirements:
    A machine with 2GB of RAM or greater.

    An Ubuntu 16.04lts operating system (Others linux distros will probably work fine).

    A Python 3.5 install or greater. This comes bundled with Ubuntu 16.04lts.

    Pip, the python package installer. This comes bundled with Ubuntu 16.04lts. However,
    you may need to edit your PATH environment variable to get this to work. In the
    command prompt type pip3. If a list of commands appear then your ready to role,
    otherwise please seek advice online to get pip to function on your Ubuntu setup.

Installation & Setup:
    To get my twitter bot running, their are a few steps you must complete first!
    First let's download it's dependencies:

        Python 3.5(If not bundled with your OS) can be downloaded here: https://www.python.org/downloads/ .
        Please follow the instruction located at this link to set up Python correctly.

        Now you should update your software repositories. Type the following into the terminal:
            sudo apt-get update
            sudo apt-get upgrade
        Enter your password if prompted and enter 'Y' if prompted.

        Next(Presuming the pip3 command is working correctly in your terminal) open a
        new terminal and type:
            pip3 install python-twitter
        To test that this step has worked correctly type the following into the terminal:
            python3
            import twitter
        If the install was a success no error should occur when importing the twitter module.

        It is also assumed you have git installed on your machine. If not you can get it by running the following:
            sudo apt-get install git
        You can tes that this has worked by simply typing the follwing into your terminal:
            git
        If a list of commands appear then you have git! Otherwise please seek advice online to get git to function on your machine.

    Now your all set and ready to go. You can clone my repository to your local disk by using the following commands:
        cd (Please insert the location of the directory you wish to place the repo in here. E.g. /home/rory/)
        git clone https://github.com/Rawd2020/Twitter_Bot

    Ok now that you have the bot downloaded please add your OAuth keys to Config.txt. This file is were
    you can store your keys and edit settings for your bot installation. The keys will give the programme access to
    your twitter account. You can create an application and an access token for it at the following link:
        https://apps.twitter.com/
    If your are unsure as to how to create the application please follow the following tutorial:
        https://www.youtube.com/watch?v=rWNYZOT0a6o
    Note:
        For the website field if you don't have a website or don't know what to fill in here just
        put in:
            http://www.google.com
        Also, leave the callback URL blank unless you know what your doing.
    Once your application is created you need to place your four keys into the Config.txt file in the following order:
        Consumer_key=hfhtfhdryhdthtgfhgtr
        Consumer_secret=dfhtbfthdfhfhfhfd
        Access_token_key=dghfhghrdhytdjhtfh3456456435
        Access_token_secret=trte5rtyrgdhtr6rt
    After that you should be good to go! :D

Testing:
    To test the setup of the twitter bot open a terminal and type the following:
        -cd (Please insert the location of the twitter bot repo in here. E.g. /home/rory/Twitter_Bot)
        -python3 Main.py
    If everything worked then you should quickly see a message, "Tweeted", printed on the screen. To verify
    a tweet was successfully made to your account just sign into your twitter and have a look. There should be a
    new tweet posted that came from the Tweets.txt file.

Miscellaneous and Troubleshooting:
    -You can add new hashtags to search for the re-tweeting job by adding them to Hashtags.txt. Add each hashtag on
    a new line excluding the has symbol from the start. For example, ig you wished to add the the hashtag #Peace,
    you would type the word:
        Peace
    on the bottom line of Hashtag.txt.

    -A similar process can be followed to add new tweets to the bots tweet job. Simply type the tweet at the bottom
    of the file (ensuring it is under twitters character limit) and save.

    -Should your API keys and token not function correctly, please ensure there is no whitespace between any of the
    keys and their equal signs. For example:
        Access_token_secret= segsgrdgbrd (INCORRECT)
        Access_token_secret=segsgrdgbrd (CORRECT)