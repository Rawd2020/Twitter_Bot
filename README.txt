Welcome to V2 of the Twitter bot.
A project by Rory Williams Doyle

System Requirements:
    A machine with 2GB of RAM or greater.

    An Ubuntu 16.04lts operating system (Others linux distros will probably work fine).

    A Python 3.5 install or greater. This comes bundled with Ubuntu 16.04lts.

    Pip, the python package installer. This comes bundled with Ubuntu 16.04lts. However,
    you may need to edit your PATH environment variable to get this to work. In the
    command prompt type pip3. If a list of commands appear then your ready to role,
    otherwise please seek advice online to get pip to function in your Ubuntu setup.

Installation:
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
        cd (Please insert the location of the directory you wish to place the repo in here. E.g. /home/rory/)
        git clone https://github.com/Rawd2020/Twitter_Bot

    Ok now that you have the bot downloaded please add a Keys.txt file into it's repo folder. This file is were
    you will 