#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.12\n")
#
# Two words "interlock" if taking alternating letters from each forms a new 
# word. For example, "shoe" and "cold" interlock to form "schooled".
#
# Question 1
# 1. Write a program that finds all pairs of words that interlock.
#    Hint: don't enumerate all pairs!
#

#
# Question 2
# 2. Can you find any words that are three-way interlocked; that is, every third 
# letter forms a word, starting from the first, second or third?
#
import bisect

fin = open('words.txt')
wlist = []


def word_list(word):
    for line in fin:
        word = line.strip()
        wlist.append(word)
    return wlist
    

def in_bisect(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word
    
def interlock(wlist):
    interlock_words = []
    for word in wlist:
        if in_bisect(wlist, word[::2]) and in_bisect(wlist, word[1::2]):
             interlock_group = (word[::2], word[1::2], word)
             interlock_words.append(interlock_group)
    return interlock_words
    
wlist = word_list(fin)
print('Results-Question 1')
print(interlock(wlist))


def three_way_interlocked(wlist):
    interlock_words = []
    for word in wlist:
        if in_bisect(wlist, word[::3]) and in_bisect(wlist, word[1::3]) and in_bisect(wlist, word[2::3]):
             interlock_group = (word[::3], word[1::3], word[2::3], word)
             interlock_words.append(interlock_group)
    return interlock_words

print('Results-Question 2')
print(three_way_interlocked(wlist))




