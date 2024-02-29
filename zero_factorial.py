def zero_factorial(num):
    fac = 1
    i = 1
    zero = 0

    while i < num:
        fac *= i
        fac *= num
        i += 1
        num -= 1
    
    if i == num:
        fac *= i

    fac_str = str(fac)
    fac_len = len(fac_str) - 1

    while fac_str[fac_len].__eq__("0"):
        zero += 1
        fac_len -= 1
    
    return zero

