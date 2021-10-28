def order_array(input_array):
    """function that rearranges the numbers in an array in smaller to larger order.\
    Input: An array of number (numbers)
    Output: The array of number rearranged in order (numbers) """
    
    for i in range(len(input_array)):
        m_index = i
        for j in range(i, len(input_array)):
            if input_array[j] < input_array[m_index]:
                m_index = j
        input_array[i], input_array[m_index] = input_array[m_index], input_array[i]
        
    return print(input_array)




def kepler_3rd(period):
    """Function that calculates the distance of a planet from the sun
    Input: Period of the planet [years]
    Output: Distance of the planet [AU]  """
    
    a_orb = 1
    earth_period = 1
    P2 = period
    P1 = earth_period
    𝛼1 = a_orb
    
    𝛼2 = 𝛼1 * (P2**2 / P1**2)**(1./3.)

    return "%.1f" %𝛼2
