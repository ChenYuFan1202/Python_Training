#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
def main():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1],sys.argv[2]))
main()

