def monotonic_array(array):
    n = len(array)
    if n == 0: return True
    first = array[0]
    last = array[n-1]

    #Monotonic Decreasing or not
    if first > last:
        for i in range(n-1):
            if array[i] < array[i+1]: return False
    #Monotonic or not
    elif first == last:
        for i in range(n-1):
            if array[i] != array[i+1]: return False
    #Monotonic Increasing or not
    else:
        for i in range(n-1):
            if array[i] > array[i+1]: return False
    return True




    
       

