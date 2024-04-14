#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_words(words):
    """takes list of cleaned words, returns count dictionary"""
    word_count = {}

    for word in words:
        count = word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count

def word_stats(word_count):
    """Takes word count dictionary and returns top and bottom five entries"""

    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])

    least_common = word_list[:5]
    most_common = word_list[-1:-6:-1]
    
    return most_common, least_common

