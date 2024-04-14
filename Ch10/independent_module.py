#!/usr/bin/env python
# coding: utf-8

# In[6]:


punct = str.maketrans("",  "", "!.,:;-?")#最後一個字串代表要刪除的東西，會沒有空格
                                         #第一個空格會被第二個空格取代


def clean_line(line):
    """changes case and removes punctuation"""
    # make all one case
    cleaned_line = line.lower()
        
    # remove punctuation
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line

def get_words(line):
    """splits line into words, and rejoins with newlines"""
    words = line.split()
    #print(words)
    return "\n".join(words) + "\n"

def count_words(words):
    """takes list of cleaned words, returns count dictionary"""
    word_count = {}
    #print(moby_words)
    for word in moby_words:
        count = word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count

def word_stats(word_count):
    """Takes word count dictionary and returns top and bottom five 
       entries"""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    least_common = word_list[:5]
    most_common = word_list[-1:-6:-1]#-1可以倒過來顯示
    return most_common, least_common

def first_step():
    with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
        for line in infile:
            cleaned_line = clean_line(line)
            cleaned_words = get_words(cleaned_line)
        
            # write all words for line
            outfile.write(cleaned_words)

def second_step():
    with open('moby_01_clean.txt') as infile:
        for word in infile:
            if word.strip():
                moby_words.append(word.strip())

def third_step():
    print("Most common words:")
    for word in most:
        print(word)

    print("\nLeast common words:")
    for word in least:
        print(word)

# infile = open("moby_01.txt")
# lines = infile.read()
# a = clean_line(lines)
# get_words(a)
#clean_line.__doc__
#first_step()
moby_words = []
#second_step()
word_count = count_words(moby_words)
most, least = word_stats(word_count)
#third_step()

