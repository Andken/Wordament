#!/usr/bin/python

import twitter

#api=twitter.Api()

api=twitter.Api(consumer_key='XBNaTJYS140ZUgv5jbD77Q',
                consumer_secret='GAUZj1D4YYdWMRFeNj2IqK0Qvnv44rJJKxlkM7eu5Q',
                access_token_key='83450267-GtsmZly7fVDgC1bx5MXnilBDJdx1P0uQ1JzxJ3BgY',
                access_token_secret='BwgE205gi1QYzubusk1hZRPAP9LXri8J2E6DVwcg')


statuses = api.GetUserTimeline("@nutonwordament")
for s in statuses:
    print s
    

#status = api.PostUpdate("Does this fucking work?")
#print status.text

