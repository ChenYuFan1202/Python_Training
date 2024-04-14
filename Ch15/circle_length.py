#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Circle:
    all_circles = []
    pi = 3.14159
    
    def __init__(self,r = 1):
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        return self.radius * self.radius * self.__class__.pi
    def length(self):
        return self.radius * 2 * self.__class__.pi
    
    @classmethod
    def total_length(cls):
        total = 0
        for c in cls.all_circles:
            total += c.length()
        return total

# class Circle:
#     pi = 3.14159
#     all_circles = []

#     def __init__(self, radius):
#         self.radius = radius
#         self.__class__.all_circles.append(self)    
        
#     def area(self):
#         return self.radius * self.radius * Circle.pi
    
#     def circumference(self):
#         return 2 * self.radius * Circle.pi
    
#     @classmethod
#     def total_circumference(cls):
#         """class method to total the circumference of all Circles """
#         total = 0
#         for c in cls.all_circles:
#             total = total + c.circumference()
#         return total