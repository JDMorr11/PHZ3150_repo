#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ft_to_m_cm(d):
    """Given a distance in feet and inches (inches input as a decimal), outputs that distance as a list in meters and centimieters [m, cm]."""
    ft = int(d)
    inch= d - ft
    m = ft / 0.3048
    cm = (inch / 2.54) + 100 * (m - int(m))
    m_cm = [int(m),round(cm)]
    return m_cm

