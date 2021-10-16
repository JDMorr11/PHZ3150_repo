#!/usr/bin/env python
# coding: utf-8

# In[14]:


def order_array(input_array):
    """sorts an array of numbers from smallest to largest."""
    import numpy as np
    unsorted = []
    for i in input_array:
        unsorted.append(i)
    sorting = []
    while len(sorting) < len(input_array):
        small = unsorted[0]
        for j in unsorted:
            if j < small:
                small = j
        sorting.append(small)
        unsorted.remove(small)
    sorted_arr = np.asarray(sorting)
    return sorted_arr


# In[16]:


def kepler_3rd(period):
    """given the period of a planet's orbit around the sun in years, returns the distance orbital distance between the planet and the sun in AU. \n Calculated using Kepler's 3rd law (P1/P2)^2 = (a1/a2)^3 where P1 and a1 are the earths period and orbital distance."""
    a = period ** (2 / 3)
    return a

