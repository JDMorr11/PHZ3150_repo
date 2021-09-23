#!/usr/bin/env python
# coding: utf-8

# In[10]:


def displacement(u_init,t,a):
    """Calculates the total displacement of a body that has initial speed u_init [m/s], during a time interval t [s], and a constant acceleration a [m/s^2]."""
    s = u_init * t + 0.5 * a * t * t
    return s

