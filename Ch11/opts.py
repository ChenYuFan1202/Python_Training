#!/usr/bin/env python
# coding: utf-8

# In[1]:


from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("indent",type=int,help="indent for report")
    parser.add_argument("input_file",help="read data form this file")
    parser.add_argument("-f","--file",dest="filename",
                       help = "write report to File",metavar = "FILE")
    parser.add_argument("-x","--xray",
                       help="specify xray strength factor")
    parser.add_argument("-q","--quiet",
                       action = "store_false",dest="verbose",default=True,
                       help = "don't print status messages to stdout")
    args = parser.parse_args()
    print("arguments:",args)
    
    
main()

