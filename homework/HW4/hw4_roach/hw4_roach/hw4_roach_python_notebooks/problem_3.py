def acceleration( u1, u2, t1, t2): #acceleration with all its variables
    """This function takes the difference of two time values [seconds] and the difference of two speed values [m/s]
    and finds acceleration. 
    Input: ( u1, u2, t1, t2)/ Output: (a) """
    
    a = (u2-u1) / (t2-t1) #My function that probably works
    
    return a