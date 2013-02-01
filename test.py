#!/usr/bin/python





import wordament

test = "babykneefacebook"

result = wordament.solve(test)

for r in result:
    tweet = "%s - %s" % (r[0], r[1])
    print "   ", tweet, r[2]
