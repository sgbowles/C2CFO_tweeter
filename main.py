#!/usr/bin/python

from twitter import *
import config

new_status = "TEST"

# config_set = {config.consumer_key, config.consumer_secret, config.access_key, config.access_secret}

tweet = Twitter(auth = OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret))

results = tweet.statuses.update(status = new_status)
