#!/usr/bin/python

wordlist = open("WORD.LST", "r").readlines()
shorter = open("WORD_3_LETTER.LST", "w")

def getScore(w):
    letter_score = {'a': 2, 
                    'b': 5,
                    'c': 3,
                    'd': 3,
                    'e': 1,
                    'f': 5,
                    'g': 4,
                    'h': 4,
                    'i': 2,
                    'j': 8,
                    'k': 6,
                    'l': 3,
                    'm': 4,
                    'n': 2,
                    'o': 2,
                    'p': 4,
                    'q': 10,
                    'r': 2,
                    's': 2,
                    't': 2,
                    'u': 4,
                    'v': 6,
                    'w': 6,
                    'x': 8,
                    'y': 5,
                    'z': 8}
    return 6

for w in wordlist:
    if (len(w.rstrip()) >= 3) and (len(w.rstrip()) <= 16):
        score = getScore(w.rstrip())
        shorter.write(w.rstrip())
        shorter.write(',')
        shorter.write(str(score))
        shorter.write('\n')




