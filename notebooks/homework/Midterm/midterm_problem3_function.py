#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def travel_distance_and_time(cities):
    """Calculates the distance time to travel from one city to another at a speed of 75 mph from a list of two cities. /n Valid cities are: Atlanta, Baltimore, Boston, Charlotte, Dallas, Denver, Miami, Minneapolis, Orlando, Sacramento, Tampa, Washington."""
    import numpy as np
    city_list = ['Atlanta', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'Denver', 'Miami', 'Minneapolis', 'Orlando', 'Sacramento', 'Tampa', 'Washington']
    start_city = cities[0]
    target_city = cities[1]
    travel_data = np.loadtxt("distances_midterm.dat", skiprows=1)
    first_city = city_list.index(start_city)
    second_city = city_list.index(target_city)
    distance = travel_data[first_city, second_city]
    print(target_city, 'is a', distance, 'mile drive from', start_city)
    time = distance / 75
    days = time / 24
    hours = 24 * (days-int(days))
    seconds = 60 * (hours - int(hours))
    print('Your trip from', start_city, 'to', target_city, 'will take', int(days), 'days', int(hours), 'hours', round(seconds), 'seconds.')

