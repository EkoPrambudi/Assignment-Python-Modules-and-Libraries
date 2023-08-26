#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

def square_root(x):
    return math.sqrt(x)

def calculate_hypotenuse(a, b):
    c_squared = a ** 2 + b ** 2
    c = square_root(c_squared)
    return c

