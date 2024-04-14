#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class EmptyStringError(Exception):
    pass

def check_empty(line):
    # raise exception if line is empty
    if not line.strip():
        raise EmptyStringError()

def check_words(words):
    for word in words:
        try:
            count = word_count.setdefault(word, 0)
        except TypeError:
            #if 'word' is not hashable, skip to next word.
            pass
        word_count[word] += 1

def check_result(word_count):
    try:
        least_common = word_list[:5]
        most_common = word_list[-1:-6:-1]
    except IndexError as e:
        # if list is empty or too short, just return list
        least_common = word_list
        most_common = list(reversed(word_list))

