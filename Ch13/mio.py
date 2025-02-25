#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
_file_object = None

def capture_output(file = "capture_file.txt"):
    global _file_object
    print("output will be sent to file:{0}".format(file))
    print("restore to normal by calling 'mio.restore_output()'")
    _file_object = open(file,"w",encoding = "utf-8")
    sys.stdout = _file_object
    
    
def restore_output():
    global _file_object
    sys.stdout = sys.__stdout__
    _file_object.close()
    print("standard output has been restored back to normal")
    
def print_file(file = "capture_file.txt"):
    f = open(file,"r",encoding = "utf-8")
    print(f.read())
    f.close()
    

def clear_file(file = "capture_file.txt"):
    f = open(file,"w")
    f.close()
    

