#!/usr/bin/python





import wordament

test = "babykneefacebook"

print test[0:4]
print test[4:8]
print test[8:12]
print test[12:16]

result = wordament.solve(test)

for r in result:
    tweet = "%s - %s" % (r[0], r[1])
    print "   ", tweet, r[2]
