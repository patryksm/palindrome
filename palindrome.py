# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:20:35 2019

@author: Patryk Smykla
"""
score = []

def is_palindrome(word):
    lngth = len(word)
    wrd = list(word)
    if lngth % 2 != 0:
        for i in range(round(lngth/2)):
            if wrd[i-1] == wrd[-i]:
                score.append(1)
            else:
                score.append(0)

    if lngth % 2 == 0:
        for i in range(int(lngth/2)):
            if wrd[i-1] == wrd[-i]:
                score.append(1)
            else:
                score.append(0)
    
    for i in score:    
        if score[i] == 0:
            return False
        else:
            return True
            



print(is_palindrome('zakopanenapokaz'))
