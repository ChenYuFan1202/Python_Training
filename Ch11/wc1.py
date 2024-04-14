#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys

def main():
    count_line = 0
    count_word = 0
    count_character = 0
    length_line = 0
    max_line = 0
    
    option = None
    param = sys.argv[1:]
    if len(param) > 1:
        option = param.pop(0).strip()
    filename = param[0]
    
    with open(filename) as infile:
        for line in infile:
            count_line += 1
            word = line.split()
            count_word += len(word)
            count_character += len(line)
            length_line = len(line)
            if length_line > max_line:
                max_line = length_line
        
    if option == "-l":
        print("行數是{}".format(count_line))
    elif option == "-w":
        print("字數是{}".format(count_word))
    elif option == "-c":
        print("字元數是{}".format(count_character))
    elif option == "-L":
        print("最長行數的長度為{}".format(max_line))   
    else:
        print("行數為{0},字數為{1},字元數為{2},最長行數的長度為{3}".format\
              (count_line,count_word,count_character,max_line))
    
    
    
if __name__ == "__main__":
    main()


# In[4]:


# a = "an apple"
# b = a.split()
# b

