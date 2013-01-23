#!/usr/bin/python

wordlist = open("WORD.LST", "r").readlines()
shorter = open("WORD_3_LETTER.LST", "w")

for w in wordlist:
    if len(w) > 3:  # need to include newline char
        shorter.write(w)





