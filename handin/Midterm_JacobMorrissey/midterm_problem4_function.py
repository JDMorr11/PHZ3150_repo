#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def trip():
    """Calculates the distance, number of necessary stops, and cost of gas to travel from one city to a pit-stop, then to another city."""
    import numpy as np
    city_list = ['Atlanta', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'Denver', 'Miami', 'Minneapolis', 'Orlando', 'Sacramento', 'Tampa', 'Washington']
    print('Please input a starting city, pit-stop city, and target city. (case sensitive)')
    start_city = str()
    pitstop_city = str()
    target_city = str()
    while len(start_city) == 0:
        start_city_in = str(input('Starting City: '))
        if start_city_in in city_list:
            start_city = start_city_in
        else:
            print('Please choose a starting city from the list.')
    while len(pitstop_city) == 0:
        pitstop_city_in = str(input('Pit-stop City: '))
        if pitstop_city_in in city_list:
            pitstop_city = pitstop_city_in
        else:
            print('Please choose a pit-stop city from the list.')
    while len(target_city) == 0:
        target_city_in = str(input('Target City: '))
        if target_city_in in city_list:
            target_city = target_city_in
        else:
            print('Please choose a target city from the list.')
    print('Start:', start_city)
    print('Pit-stop:', pitstop_city)
    print('End:', target_city)
    travel_data = np.loadtxt("distances_midterm.dat", skiprows=1)
    first_city = city_list.index(start_city)
    second_city = city_list.index(pitstop_city)
    third_city = city_list.index(target_city)
    distance1 = int(travel_data[first_city, second_city]) 
    distance2 = int(travel_data[second_city,third_city])
    print(pitstop_city, 'is a', distance1, 'mile drive from', start_city, 'and', target_city, 'is a', distance2, 'mile drive from', pitstop_city)
    stops1 = int(np.ceil(distance1 / (24.9 * 16)))
    stops2 = int(np.ceil(distance2 / (24.9 * 16)))
    cost = float(2.4 * (distance1 + distance2)/24.9)
    print('You need to stop for gas', stops1, 'times between', start_city, 'and', pitstop_city)
    print('You need to stop for gas', stops2, 'times between', pitstop_city, 'and', target_city)
    print('The total cost of gas will be $', "{0:.2f}".format(cost))


# In[3]:




