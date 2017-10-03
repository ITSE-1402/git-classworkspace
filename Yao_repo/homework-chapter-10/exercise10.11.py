#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 10.11\n")
#
# Question 1
# 1. Two words are a "reverse pair" if each is the reverse of the other. Write 
# a program that finds all the reverse pairs in the word list.
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
        
def reverse_pair(wlist):
    reverse_pair_list = []
    for word in wlist:
        if in_bisect(wlist, word[::-1]):
            pair = (word, word[::-1])
            reverse_pair_list.append(pair)
    return reverse_pair_list


wlist = word_list(fin)

print(reverse_pair(wlist))
