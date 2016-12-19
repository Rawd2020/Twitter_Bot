 WELCOME TO TWITTER BOT! :D

 Created by: Rory Williams Doyle
 Created on: 18/12/2016
 Last modified: 18/12/2016
 Version: 2.0
 README last update: 19/12/2016

System Requirements:
    A machine with 2GB of RAM or greater.

    An Ubuntu 16.04lts operating system (Others linux distros will probably work fine).

    A Python 3.5 install or greater. This comes bundled with Ubuntu 16.04lts.

    Pip, the python package installer. This comes bundled with Ubuntu 16.04lts. However,
    you may need to edit your PATH environment variable to get this to work. In the
    command prompt type pip3. If a list of commands appear then your ready to role,
    otherwise please seek advice online to get pip to function in your Ubuntu setup.

Installation & Setup:
    To get my twitter bot running, their are a few steps you must complete first!
    First let's download our dependencies:

        Python 3.5(If not bundled with your OS) can be downloaded here: https://www.python.org/downloads/ .
        Please follow the instruction located at this link to set up Python correctly.

        Next(Presuming the pip3 command is working correctly in your terminal) open a
        new terminal and type:
            pip3 install python-twitter
        To test that this step has worked correctly type the following into the terminal:
            -python3
            -import twitter
        If the install was a success no error should occur when importing the twitter module.

    Now your all set and ready to go. You can clone my repository to your local disk by using the following commands:
        -cd (Please insert the location of the directory you wish to place the repo in here. E.g. /home/rory/)
        -git clone https://github.com/Rawd2020/Twitter_Bot

    Ok now that you have the bot downloaded please add a Keys.txt file into it's repo folder. This file is were
    you will put the keys for the OAuth security of your twitter account. This will give the programme access to
    your twitter account. You can create an application and an access token for it at the following link:
        https://apps.twitter.com/
    If your are unsure as to how to create the application please follow the following tutorial:
        https://www.youtube.com/watch?v=rWNYZOT0a6o
    Note:
        For the website field if you don't have a website or don't know what to fill in here just
        put in:
            http://www.google.com
        Also, leave the callback URL blank unless you know what your doing.
    Once your application is created you need to place your four keys into the Keys.txt file in the following order:
        Line 1 = Consumer Key (API Key)
        Line 2 = Consumer Secret (API Secret)
        Line 3 = Access Token
        Line 4 = Access Token Secret
    After that you should be good to go! :D

Testing:
    To test the setup of the twitter bot open a terminal and type the following:
        -cd (Please insert the location of the twitter bot repo in here. E.g. /home/rory/Twitter_Bot)
        -python3 Main.py
    If everything worked then you should quickly see a message, "Tweeted", printed on the screen. To verify
    a tweet was successfully made to your account just sign into your twitter and have a look. There should be a
    new tweet posted that came from the Tweets.txt file.