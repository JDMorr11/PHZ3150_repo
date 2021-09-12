#!/usr/bin/env python
# coding: utf-8

# In[1]:


def acceleration(u1, u2, t1, t2):
    """Calculates the acceleration, a [m / s^2], from the velocities, u1 and u2 [m /s], at corresponding times, t1 and t2 [s]."""
    a = ( u2 - u1) / ( t2 - t1)
    return a

