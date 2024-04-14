#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Color:
    def __init__(self,red,green,blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return "Color: R={0:1d}, G={1:d}, B={2:1d}".format(self._red,
                                                         self._green,
                                                         self._blue)
# 1d = d代表空多少格然後是靠右,0、1、2就是順序
#如果是f"{變數:1(直接打數字)}"