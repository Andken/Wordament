#!/usr/bin/python

wordlist = open("WORD.LST", "r").readlines()
shorter = open("WORD_3_LETTER.LST", "w")

for w in wordlist:
    if (len(w.rstrip()) >= 3) and (len(w.rstrip()) <= 16):
        shorter.write(w)





