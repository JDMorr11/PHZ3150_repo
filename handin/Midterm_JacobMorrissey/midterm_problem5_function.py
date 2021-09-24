#!/usr/bin/env python
# coding: utf-8

# In[22]:


def travel_distance_and_time():
    """Calculates the distance time to travel from one city to another at a speed of 75 mph from a list of two cities. /n Valid cities are: Atlanta, Baltimore, Boston, Charlotte, Dallas, Denver, Miami, Minneapolis, Orlando, Sacramento, Tampa, Washington."""
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
    distance = travel_data[first_city, second_city]
    print(target_city, 'is a', distance, 'mile drive from', start_city)
    time = distance / 75
    days = time / 24
    hours = 24 * (days-int(days))
    seconds = 60 * (hours - int(hours))
    print('Your trip from', start_city, 'to', target_city, 'will take', int(days), 'days', int(hours), 'hours', round(seconds), 'seconds.')


# In[23]:


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
    cost = float(2.4 * 16 * (stops1 + stops2))
    print('You need to stop for gas', stops1, 'times between', start_city, 'and', pitstop_city)
    print('You need to stop for gas', stops2, 'times between', pitstop_city, 'and', target_city)
    print('The total cost of gas will be $', "{0:.2f}".format(cost))


# In[27]:


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
    cost = float(2.4 * 16 * (stops1 + stops2))
    print('You will be stopping at', city_list[min_tot_dist_ind], 'between', start_city, 'and', target_city)
    print('The total trip will be ', int(min_distance), 'miles')
    print('You need to stop for gas', stops1, 'times between', start_city, 'and', city_list[min_tot_dist_ind])
    print('You need to stop for gas', stops2, 'times between', city_list[min_tot_dist_ind], 'and', target_city)
    print('The total cost of gas will be $', "{0:.2f}".format(cost))

