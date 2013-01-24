#!/usr/bin/python

import copy

def inBox(xin, yin, w, b):
    if len(w) == 0:
        return True

    if xin==0 and yin==0:
        for x, y in ((0, 1), (1,1), (1,0)):
            if b[x][y] == w[0]:
                new_b = copy.deepcopy(b)
                new_b[x][y] = '?'
                if inBox(x,y, w[1:], new_b):
                    return True
    elif xin==3 and yin==0: 
        for x, y in ((2,0), (2,1), (3,1)):
            if b[x][y] == w[0]:
                new_b = copy.deepcopy(b)
                new_b[x][y] = '?'
                if inBox(x,y, w[1:], new_b):
                    return True
    elif xin==0 and yin==3: 
        for x, y in ((0,2), (1,2), (1,3)):
            if b[x][y] == w[0]:
                new_b = copy.deepcopy(b)
                new_b[x][y] = '?'
                if inBox(x,y, w[1:], new_b):
                    return True
    elif xin==3 and yin==3: 
        for x, y in ((3,2), (2,2), (2,3)):
            if b[x][y] == w[0]:
                new_b = copy.deepcopy(b)
                new_b[x][y] = '?'
                if inBox(x,y, w[1:], new_b):
                    return True
    elif xin==0:
        for x in (0,1):
            for y in (yin-1, yin, yin+1):
                if not (x==0 and y==yin):
                    if b[x][y] == w[0]:
                        new_b = copy.deepcopy(b)
                        new_b[x][y] = '?'
                        if inBox(x,y, w[1:], new_b):
                            return True
    elif xin==3:
        for x in (2,3):
            for y in (yin-1, yin, yin+1):
                if not (x==3 and y==yin):
                    if b[x][y] == w[0]:
                        new_b = copy.deepcopy(b)
                        new_b[x][y] = '?'
                        if inBox(x,y, w[1:], new_b):
                            return True
    elif yin==0:
        for x in (xin-1, xin, xin+1):
            for y in (0,1):
                if not (x==xin and y==0):
                    if b[x][y] == w[0]:
                        new_b = copy.deepcopy(b)
                        new_b[x][y] = '?'
                        if inBox(x,y, w[1:], new_b):
                            return True
    elif yin==3:
        for x in (xin-1, xin, xin+1):
            for y in (2,3):
                if not (y==3 and x==xin):
                    if b[x][y] == w[0]:
                        new_b = copy.deepcopy(b)
                        new_b[x][y] = '?'
                        if inBox(x,y, w[1:], new_b):
                            return True
    else:
        for x in (xin-1, xin, xin+1):
            for y in (yin-1, yin, yin+1):
                if not (y==yin and x==xin):
                    if b[x][y] == w[0]:
                        new_b = copy.deepcopy(b)
                        new_b[x][y] = '?'
                        if inBox(x,y, w[1:], new_b):
                            return True
    return False

def isPossible(letters, b_sorted):
    return True

def inBoxFirst(w, letters, b, b_sorted):
    if not isPossible(letters, b_sorted):
        return False

    for x in range(4):
        for y in range(4):
            if b[x][y] == w[0]:
                new_b = copy.deepcopy(b)
                new_b[x][y] = '?'
                if inBox(x,y,w[1:], new_b):
                    return True
    return False


y = raw_input("?: ")

# TEST BOX
#baby
#over
#open
#knee
#y = "babyoveropenknee"

b = (list(y)[0:4], list(y)[4:8], list(y)[8:12], list(y)[12:16])
y_sorted = ''.join(sorted(y))

wordlist = open("WORD_3_LETTER.LST", "r").readlines()

for pair in wordlist:
    tuple = pair.rstrip().split(' ')
    if inBoxFirst(list(tuple[0]), list(tuple[1]), b, y_sorted):
        print tuple[0], tuple[2]



