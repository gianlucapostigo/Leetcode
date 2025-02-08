def sorted_squared2(array):
    n = len(array)
    left, right = 0, n - 1
    res = [0]*n
    for i in reversed(range(n)):
        if array[left]**2 > array[right]**2:
            res[i] = array[left]**2
            left += 1
        else:
            res[i] = array[right]**2
            right -= 1
    return res