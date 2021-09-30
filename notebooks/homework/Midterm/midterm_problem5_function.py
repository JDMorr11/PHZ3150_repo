#!/usr/bin/env python
# coding: utf-8

# In[3]:


def min_trip():
    """Given a starting city and destination city, finds a pit-stop city to minimize the distance traveled, and calculates the distance, number of rest stops needed, and cost of gas."""
    import numpy as np
    city_list = ['Atlanta', 'Baltimore', 'Boston', 'Charlotte', 'Dallas', 'Denver', 'Miami', 'Minneapolis', 'Orlando', 'Sacramento', 'Tampa', 'Washington']
    print('Please input a starting city and target city. (case sensitive)')
    start_city = str()
    target_city = str()
    while len(start_city) == 0:
        start_city_in = str(input('Starting City: '))
        if start_city_in in city_list:
            start_city = start_city_in
        else:
            print('Please choose a starting city from the list.')
    while len(target_city) == 0:
        target_city_in = str(input('Target City: '))
        if target_city_in in city_list:
            target_city = target_city_in
        else:
            print('Please choose a target city from the list.')
    print('Start:', start_city)
    print('End:', target_city)
    travel_data = np.loadtxt("distances_midterm.dat", skiprows=1)
    first_city = city_list.index(start_city)
    second_city = city_list.index(target_city)
    cities = [start_city, target_city]
    distances = []
    for i in range(len(city_list)):
        if city_list[i] in cities:
            distances.append(50000)
        else:
            trip_distance = travel_data[first_city, i] + travel_data[i, second_city]
            distances.append(trip_distance)
    min_distance = min(distances)
    min_tot_dist_ind = distances.index(min_distance)
    distance1 = int(travel_data[first_city, min_tot_dist_ind]) 
    distance2 = int(travel_data[min_tot_dist_ind,second_city])
    stops1 = int(np.ceil(distance1 / (24.9 * 16)))
    stops2 = int(np.ceil(distance2 / (24.9 * 16)))
    cost = float(2.4 * (distance1 + distance2)/24.9)
    print('You will be stopping at', city_list[min_tot_dist_ind], 'between', start_city, 'and', target_city)
    print('The total trip will be ', int(min_distance), 'miles')
    print('You need to stop for gas', stops1, 'times between', start_city, 'and', city_list[min_tot_dist_ind])
    print('You need to stop for gas', stops2, 'times between', city_list[min_tot_dist_ind], 'and', target_city)
    print('The total cost of gas will be $', "{0:.2f}".format(cost))

