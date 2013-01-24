#!/usr/bin/python

wordlist = open("WORD.LST", "r").readlines()

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
    score = 0
    for letter in list(w):
        score += letter_score[letter]

    if len(w) == 4 or len(w) == 5:
        score *= 1.5
    elif len(w) == 6 or len(w) == 7:
        score *= 2
    elif len(w) >= 8:
        score *= 3

    return int(score)

result = []

for w in wordlist:
    if (len(w.rstrip()) >= 3) and (len(w.rstrip()) <= 16):
        result.append((w.rstrip(), getScore(w.rstrip())))

scorelist=sorted(result, key=lambda score: score[1])
scorelist.reverse()

for pair in scorelist:
    print pair[0], pair[1]

