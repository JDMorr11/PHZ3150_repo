#!/usr/bin/env python
# coding: utf-8

# In[12]:


def quadratic(a,b,c):
    """Gives a list containing the roots of a parabola. Input the coefficients (a,b,c) for the function ax^2 + bx + c = 0"""
    import numpy as np
    x1 = ( -np.sqrt( (b*b) - 4 * a * c ) - b ) / (2 * a)
    x2 = ( np.sqrt( (b*b) - 4 * a * c ) - b ) / (2 * a)
    roots = [x1, x2]
    return roots

