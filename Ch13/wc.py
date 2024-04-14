#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os,sys

count_word = 0
count_tuple = 0

parameter = sys.argv[1:]
file_or_sen = parameter[0]
option = parameter[1]

if (os.path.isfile(file_or_sen) == True) & (option == "-m"):
    with open(file_or_sen,"r",encoding = "utf-8") as f:
        words = f.read()
        count_word += len(words)
elif (os.path.isfile(file_or_sen) == True) & (option == "-c"):
    with open(file_or_sen,"rb") as f:
        byte = f.read()
        count_tuple += len(byte)
elif (os.path.isfile(file_or_sen) == False) & (option == "-m"):
    words = file_or_sen
    count_word += len(words)
elif (os.path.isfile(file_or_sen) == False) & (option == "-c"):
    byte = file_or_sen.encode("utf-8")
    count_tuple += len(byte)

if option == "-m":
    print("字元數為{}".format(count_word))
elif option == "-c":
    print("位元組為{}".format(count_tuple))

#print(sys.argv)
    