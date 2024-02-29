def max_number(int_array):
    index = 0
    max = int_array[0]
    i = 1
    half_len_array = (len(int_array) // 2)  + (len(int_array) % 2 > 0)

    while i <= half_len_array:
        if int_array[-i] >= max:
            max = int_array[-i]
            index = -i
        
        if int_array[i-1] >= max:
            max = int_array[i-1]
            index = i-1
        
        i += 1

    if index < 0:
        index += len(int_array)

    return index


