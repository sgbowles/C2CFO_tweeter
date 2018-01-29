#!/usr/bin/python

from twitter import *
import config
from team_list import *
import random
import time

full_teams = get_team_list()

random.shuffle(full_teams)

tweet = Twitter(auth = OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret))

count = full_teams.__len__()

firstNum = count
secNum = count - 4

output = "Draft selection results " + str(firstNum) + " - " + str(secNum) + ":\n"

for teamName in reversed(full_teams):
    output += str(count) + ": " + teamName + "\n"
    if count == secNum:
        results = tweet.statuses.update(status=output)
        firstNum -= 5
        secNum -= 5
        output = "Draft selection results " + str(firstNum) + " - " + str(secNum) + ":\n"
        time.sleep(5)
    count -= 1




