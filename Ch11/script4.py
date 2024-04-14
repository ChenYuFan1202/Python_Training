#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import fileinput
def main():
    for line in fileinput.input():
        if not line.startswith("##"):
            print(line,end="\n")
main()

