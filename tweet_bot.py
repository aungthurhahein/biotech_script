#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import os
import time
import string
import twitter

# The delay between queries in seconds
REQUEST_DELAY = 2
# Twitter account management
TWITTER_USERNAME = 'Atrhein'
# The date format, to give the Twitter API
DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'
# The file name for recording history, "made" tweets
LOG_FILE = 'history.txt'

api = twitter.Api()

while True:
    statuses = api.GetUserTimeline(TWITTER_USERNAME)
    try:
        command = statuses[0]
    except IndexError:
        command = None

    if isinstance(command, twitter.Status):
        with open(LOG_FILE, 'a+') as f:
            history = string.split(f.read(), "\n")
            if not str(command.id) in history:
                os.system(command.text)
                f.write(str(command.id) + "\n")
        f.closed

    time.sleep(REQUEST_DELAY)