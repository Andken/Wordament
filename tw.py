#!/usr/bin/python

import twitter
from datetime import datetime, timedelta
from email.utils import parsedate_tz
import time
import wordament

# from http://stackoverflow.com/questions/7703865/going-from-twitter-date-to-python-datetime-date
def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

api=twitter.Api(consumer_key='XBNaTJYS140ZUgv5jbD77Q',
                consumer_secret='GAUZj1D4YYdWMRFeNj2IqK0Qvnv44rJJKxlkM7eu5Q',
                access_token_key='83450267-GtsmZly7fVDgC1bx5MXnilBDJdx1P0uQ1JzxJ3BgY',
                access_token_secret='BwgE205gi1QYzubusk1hZRPAP9LXri8J2E6DVwcg')


orig_statuses = api.GetUserTimeline("@nutonwordament")

starting_post_time = to_datetime(orig_statuses[0].created_at)

while 1:
    statuses = api.GetUserTimeline("@nutonwordament")
    latest_post_time = to_datetime(statuses[0].created_at)
    if latest_post_time > starting_post_time:
        print "new tweet: ", statuses[0].text
        starting_post_time = latest_post_time
        if len(statuses[0].text) == 16:
            results = wordament.solve(statuses[0].text)
            for r in results:
                tweet = "%s - %s" % (r[0], r[1])
                api.PostUpdate(tweet)

    time.sleep(1)


